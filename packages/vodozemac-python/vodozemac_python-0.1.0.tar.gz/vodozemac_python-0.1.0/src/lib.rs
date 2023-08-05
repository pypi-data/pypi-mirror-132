use std::collections::HashMap;

use pyo3::prelude::*;

#[pyclass]
struct Account {
    inner: vodozemac::olm::Account,
}

#[pymethods]
impl Account {
    #[new]
    fn new() -> Self {
        Self {
            inner: vodozemac::olm::Account::new(),
        }
    }

    #[getter]
    fn ed25519_key(&self) -> &str {
        self.inner.ed25519_key_encoded()
    }

    #[getter]
    fn curve25519_key(&self) -> &str {
        self.inner.curve25519_key_encoded()
    }

    fn sign(&self, message: &str) -> String {
        self.inner.sign(message)
    }

    #[getter]
    fn one_time_keys(&self) -> HashMap<String, String> {
        self.inner.one_time_keys_encoded()
    }

    fn generate_one_time_keys(&mut self, count: usize) {
        self.inner.generate_one_time_keys(count)
    }

    #[getter]
    fn fallback_key(&self) -> HashMap<String, String> {
        self.inner
            .fallback_key()
            .into_iter()
            .map(|(k, v)| (k.to_base64(), v))
            .collect()
    }

    fn generate_fallback_key(&mut self) {
        self.inner.generate_fallback_key()
    }

    fn create_outbound_session(&self, identity_key: &str, one_time_key: &str) -> Session {
        let identity_key = vodozemac::Curve25519PublicKey::from_base64(identity_key).unwrap();
        let one_time_key = vodozemac::Curve25519PublicKey::from_base64(one_time_key).unwrap();
        let session = self
            .inner
            .create_outbound_session(identity_key, one_time_key);

        Session { inner: session }
    }

    fn create_inbound_session(&mut self, identity_key: &str, message: &OlmMessage) -> Session {
        let identity_key = vodozemac::Curve25519PublicKey::from_base64(identity_key).unwrap();

        let message = vodozemac::olm::OlmMessage::from_type_and_ciphertext(
            message.message_type,
            message.ciphertext.to_owned(),
        )
        .unwrap();

        if let vodozemac::olm::OlmMessage::PreKey(message) = message {
            let session = self
                .inner
                .create_inbound_session(&identity_key, &message)
                .unwrap();

            Session { inner: session }
        } else {
            panic!("Invalid message type")
        }
    }
}

#[pyclass]
struct OlmMessage {
    #[pyo3(get)]
    ciphertext: String,
    #[pyo3(get)]
    message_type: usize,
}

#[pyclass]
struct Session {
    inner: vodozemac::olm::Session,
}

#[pymethods]
impl Session {
    #[getter]
    fn session_id(&self) -> String {
        self.inner.session_id()
    }

    fn encrypt(&mut self, plaintext: &str) -> OlmMessage {
        let message = self.inner.encrypt(plaintext);

        let (message_type, ciphertext) = message.to_tuple();

        OlmMessage {
            ciphertext,
            message_type,
        }
    }

    fn decrypt(&mut self, message: &OlmMessage) -> String {
        let message = vodozemac::olm::OlmMessage::from_type_and_ciphertext(
            message.message_type,
            message.ciphertext.to_owned(),
        )
        .unwrap();

        self.inner.decrypt(&message).unwrap()
    }
}

#[pymodule]
#[pyo3(name = "vodozemac")]
fn mymodule(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Account>()?;
    m.add_class::<Session>()?;
    Ok(())
}
