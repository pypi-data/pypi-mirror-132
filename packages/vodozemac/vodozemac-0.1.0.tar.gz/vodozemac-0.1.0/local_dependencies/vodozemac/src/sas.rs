// Copyright 2021 Damir Jelić, Denis Kasak
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

//! User-friendly key verification using short authentication strings (SAS).
//!
//! The verification process is heavily inspired by Phil Zimmermann’s [ZRTP]
//! key agreement handshake. A core part of key agreement in [ZRTP] is the
//! *hash commitment*: the party that begins the key sharing process sends
//! a *hash* of their part of the Diffie-Hellman exchange but does not send the
//! part itself exchange until they had received the other party’s part.
//!
//! The verification process can be used to verify the Ed25519 identity key of
//! an [`Account`].
//!
//! # Examples
//!
//! ```rust
//! use vodozemac::sas::Sas;
//!
//! let alice = Sas::new();
//! let bob = Sas::new();
//!
//! let bob_public_key = bob.public_key();
//!
//! let bob = bob.diffie_hellman(alice.public_key());
//! let alice = alice.diffie_hellman(bob_public_key);
//!
//! let alice_bytes = alice.bytes("AGREED_INFO");
//! let bob_bytes = bob.bytes("AGREED_INFO");
//!
//! let alice_emojis = alice_bytes.emoji_index();
//! let bob_emojis = bob_bytes.emoji_index();
//!
//! assert_eq!(alice_emojis, bob_emojis);
//! ```
//!
//! [`Account`]: crate::olm::Account
//! [ZRTP]: https://tools.ietf.org/html/rfc6189#section-4.4.1

use hkdf::Hkdf;
use hmac::{digest::MacError, Hmac, Mac};
use rand::thread_rng;
use sha2::Sha256;
use thiserror::Error;
use x25519_dalek::{EphemeralSecret, SharedSecret};

use crate::{
    utilities::{base64_decode, base64_encode},
    Curve25519KeyError, Curve25519PublicKey,
};

type HmacSha256Key = [u8; 32];

/// Error type describing failures that can happen during the key verification.
#[derive(Debug, Error)]
pub enum SasError {
    /// The MAC code that was given wasn't valid base64.
    #[error("The SAS MAC wasn't valid base64: {0}")]
    Base64(#[from] base64::DecodeError),
    /// The MAC failed to be validated.
    #[error("The SAS MAC validation didn't succeed: {0}")]
    Mac(#[from] MacError),
}

/// A struct representing a short auth string verification object.
///
/// This object can be used to establish a shared secret to perform the short
/// auth string based key verification.
pub struct Sas {
    secret_key: EphemeralSecret,
    public_key: Curve25519PublicKey,
    encoded_public_key: String,
}

/// A struct representing a short auth string verification object where the
/// shared secret has been established.
///
/// This object can be used to generate the short auth string and calculate and
/// verify a MAC that protects information about the keys being verified.
pub struct EstablishedSas {
    shared_secret: SharedSecret,
}

/// Bytes generated from an shared secret that can be used as the short auth
/// string.
#[derive(Debug, Clone, PartialEq)]
pub struct SasBytes {
    bytes: [u8; 6],
}

impl SasBytes {
    /// Get the index of 7 emojis that can be presented to users to perform the
    /// key verification
    ///
    /// The table that maps the index to an emoji can be found in the [spec].
    ///
    /// [spec]: https://spec.matrix.org/unstable/client-server-api/#sas-method-emoji
    pub fn emoji_index(&self) -> [u8; 7] {
        Self::bytes_to_emoji_index(&self.bytes)
    }

    /// Get the three decimal numbers that can be presented to users to perform
    /// the key verification, as described in the [spec]
    ///
    /// [spec]: https://spec.matrix.org/unstable/client-server-api/#sas-method-emoji
    pub fn decimlas(&self) -> (u16, u16, u16) {
        Self::bytes_to_decimal(&self.bytes)
    }

    /// Get the raw bytes of the short auth string that can be converted to an
    /// emoji, or decimal representation.
    pub fn as_bytes(&self) -> &[u8; 6] {
        &self.bytes
    }

    /// Split the first 42 bits of our 6 bytes into 7 groups of 6 bits. The 7
    /// groups of 6 bits represent an emoji index from the [spec].
    ///
    /// [spec]: https://spec.matrix.org/unstable/client-server-api/#sas-method-emoji
    fn bytes_to_emoji_index(bytes: &[u8; 6]) -> [u8; 7] {
        let bytes: Vec<u64> = bytes.iter().map(|b| *b as u64).collect();
        // Join the 6 bytes into one 64 bit unsigned int. This u64 will contain 48
        // bits from our 6 bytes.
        let mut num: u64 = bytes[0] << 40;
        num += bytes[1] << 32;
        num += bytes[2] << 24;
        num += bytes[3] << 16;
        num += bytes[4] << 8;
        num += bytes[5];

        // Take the top 42 bits of our 48 bits from the u64 and convert each 6 bits
        // into a 6 bit number.
        [
            ((num >> 42) & 63) as u8,
            ((num >> 36) & 63) as u8,
            ((num >> 30) & 63) as u8,
            ((num >> 24) & 63) as u8,
            ((num >> 18) & 63) as u8,
            ((num >> 12) & 63) as u8,
            ((num >> 6) & 63) as u8,
        ]
    }

    /// Convert the given bytes into three decimals. The 6th byte is ignored,
    /// it's used for the emoji index conversion.
    fn bytes_to_decimal(bytes: &[u8; 6]) -> (u16, u16, u16) {
        let bytes: Vec<u16> = bytes.iter().map(|b| *b as u16).collect();

        // This bitwise operation is taken from the [spec]
        // [spec]: https://matrix.org/docs/spec/client_server/latest#sas-method-decimal
        let first = bytes[0] << 5 | bytes[1] >> 3;
        let second = (bytes[1] & 0x7) << 10 | bytes[2] << 2 | bytes[3] >> 6;
        let third = (bytes[3] & 0x3F) << 7 | bytes[4] >> 1;

        (first + 1000, second + 1000, third + 1000)
    }
}

impl Default for Sas {
    fn default() -> Self {
        Self::new()
    }
}

impl Sas {
    /// Create a new random verification object
    ///
    /// This creates an ephemeral curve25519 keypair that can be used to
    /// establish a shared secret.
    pub fn new() -> Self {
        let rng = thread_rng();

        let secret_key = EphemeralSecret::new(rng);
        let public_key = Curve25519PublicKey::from(&secret_key);
        let encoded_public_key = base64_encode(public_key.as_bytes());

        Self { secret_key, public_key, encoded_public_key }
    }

    /// Get the public key that can be used to establish a shared secret.
    pub fn public_key(&self) -> Curve25519PublicKey {
        self.public_key
    }

    /// Get the public key as a base64 encoded string.
    pub fn public_key_encoded(&self) -> &str {
        &self.encoded_public_key
    }

    /// Establishes a SAS secret by performing a DH handshake with another
    /// public key.
    pub fn diffie_hellman(self, other_public_key: Curve25519PublicKey) -> EstablishedSas {
        let shared_secret = self.secret_key.diffie_hellman(&other_public_key.inner);

        EstablishedSas { shared_secret }
    }

    /// Establishes a SAS secret by performing a DH handshake with another
    /// public key in "raw", base64-encoded form.
    pub fn diffie_hellman_with_raw(
        self,
        other_public_key: &str,
    ) -> Result<EstablishedSas, Curve25519KeyError> {
        let other_public_key = Curve25519PublicKey::from_base64(other_public_key)?;

        let shared_secret = self.secret_key.diffie_hellman(&other_public_key.inner);

        Ok(EstablishedSas { shared_secret })
    }
}

impl EstablishedSas {
    /// Generate [`SasBytes`] using HKDF with the shared secret as the input key
    /// material.
    ///
    /// The info string should be agreed upon beforehand, both parties need to
    /// use the same info string.
    pub fn bytes(&self, info: &str) -> SasBytes {
        let mut bytes = [0u8; 6];
        let byte_vec = self.bytes_raw(info, 6);

        bytes.copy_from_slice(&byte_vec);

        SasBytes { bytes }
    }

    /// Generate the given number  of bytes using HKDF with the shared secret
    /// as the input key material.
    ///
    /// The info string should be agreed upon beforehand, both parties need to
    /// use the same info string.
    pub fn bytes_raw(&self, info: &str, count: usize) -> Vec<u8> {
        let mut output = vec![0u8; count];
        let hkdf = self.get_hkdf();

        hkdf.expand(info.as_bytes(), &mut output[0..count]).expect("Can't generate the SAS bytes");

        output
    }

    /// Calculate a MAC for the given input using the info string as additional
    /// data.
    ///
    ///
    /// This should be used to calculate a MAC of the ed25519 identity key of an
    /// [`Account`]
    ///
    /// The MAC is returned as a base64 encoded string.
    ///
    /// [`Account`]: crate::olm::Account
    pub fn calculate_mac(&self, input: &str, info: &str) -> String {
        let mut mac = self.get_mac(info);

        mac.update(input.as_ref());

        base64_encode(mac.finalize().into_bytes())
    }

    /// Verify a MAC that was previously created using the
    /// [`EstablishedSas::calculate_mac()`] method.
    ///
    /// Users should calculate a MAC and send it to the other side, they should
    /// then verify each other's MAC using this method.
    pub fn verify_mac(&self, input: &str, info: &str, tag: &str) -> Result<(), SasError> {
        let tag = base64_decode(tag)?;

        let mut mac = self.get_mac(info);
        mac.update(input.as_bytes());

        Ok(mac.verify_slice(&tag)?)
    }

    fn get_hkdf(&self) -> Hkdf<Sha256> {
        Hkdf::new(None, self.shared_secret.as_bytes())
    }

    fn get_mac_key(&self, info: &str) -> HmacSha256Key {
        let mut mac_key = [0u8; 32];
        let hkdf = self.get_hkdf();

        hkdf.expand(info.as_bytes(), &mut mac_key).expect("Can't expand the MAC key");

        mac_key
    }

    fn get_mac(&self, info: &str) -> Hmac<Sha256> {
        let mac_key = self.get_mac_key(info);
        Hmac::<Sha256>::new_from_slice(&mac_key).expect("Can't create a HMAC object")
    }
}

#[cfg(test)]
mod test {
    use anyhow::Result;
    use olm_rs::sas::OlmSas;
    use proptest::prelude::*;

    use super::{Sas, SasBytes};

    #[test]
    fn generate_bytes() -> Result<()> {
        let mut olm = OlmSas::new();
        let dalek = Sas::new();

        olm.set_their_public_key(dalek.public_key_encoded().to_string())
            .expect("Couldn't set the public key for libolm");
        let established = dalek.diffie_hellman_with_raw(&olm.public_key())?;

        assert_eq!(
            olm.generate_bytes("TEST", 10).expect("libolm coulnd't generate SAS bytes"),
            established.bytes_raw("TEST", 10)
        );

        Ok(())
    }

    #[test]
    // Allowed to fail due to https://gitlab.matrix.org/matrix-org/olm/-/merge_requests/16
    fn calculate_mac() -> Result<()> {
        let mut olm = OlmSas::new();
        let dalek = Sas::new();

        olm.set_their_public_key(dalek.public_key_encoded().to_string())
            .expect("Couldn't set the public key for libolm");
        let established = dalek.diffie_hellman_with_raw(&olm.public_key())?;

        let olm_mac =
            olm.calculate_mac_fixed_base64("", "").expect("libolm couldn't calculate a MAC");
        assert_eq!(olm_mac, established.calculate_mac("", ""));

        established.verify_mac("", "", olm_mac.as_str())?;

        Ok(())
    }

    #[test]
    fn emoji_generation() {
        let bytes: [u8; 6] = [0, 0, 0, 0, 0, 0];
        let index: [u8; 7] = [0, 0, 0, 0, 0, 0, 0];
        assert_eq!(SasBytes::bytes_to_emoji_index(&bytes), index.as_ref());

        let bytes: [u8; 6] = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF];
        let index: [u8; 7] = [63, 63, 63, 63, 63, 63, 63];
        assert_eq!(SasBytes::bytes_to_emoji_index(&bytes), index.as_ref());
    }

    #[test]
    fn decimal_generation() {
        let bytes: [u8; 6] = [0, 0, 0, 0, 0, 0];
        let result = SasBytes::bytes_to_decimal(&bytes);

        assert_eq!(result, (1000, 1000, 1000));

        let bytes: [u8; 6] = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF];
        let result = SasBytes::bytes_to_decimal(&bytes);
        assert_eq!(result, (9191, 9191, 9191));
    }

    proptest! {
        #[test]
        fn proptest_emoji(bytes in prop::array::uniform6(0u8..)) {
            let numbers = SasBytes::bytes_to_emoji_index(&bytes);

            for number in numbers.iter() {
                prop_assert!(*number < 64);
            }
        }
    }

    proptest! {
        #[test]
        fn proptest_decimals(bytes in prop::array::uniform6(0u8..)) {
            let (first, second, third) = SasBytes::bytes_to_decimal(&bytes);

            prop_assert!((1000..=9191).contains(&first));
            prop_assert!((1000..=9191).contains(&second));
            prop_assert!((1000..=9191).contains(&third));
        }
    }
}
