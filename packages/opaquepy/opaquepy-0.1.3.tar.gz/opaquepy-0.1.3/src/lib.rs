use curve25519_dalek;
use curve25519_dalek::ristretto::RistrettoPoint;
use opaque_ke::ciphersuite::CipherSuite;
use sha2;
use rand::{rngs::OsRng};
use opaque_ke::{CredentialFinalization, CredentialRequest,
                RegistrationRequest, RegistrationUpload, ServerLogin, ServerLoginFinishResult,
                ServerLoginStartParameters, ServerLoginStartResult, ServerRegistration,
                ServerRegistrationStartResult};
use opaque_ke::keypair::{Key, KeyPair};
use pyo3::prelude::*;
use scrypt::ScryptParams;
use base64;
use base64::DecodeError;
use opaque_ke::errors::{PakeError, ProtocolError};
use pyo3::exceptions::PyValueError;

struct DefaultCipher;
impl CipherSuite for DefaultCipher {
    type Group = curve25519_dalek::ristretto::RistrettoPoint;
    type KeyExchange = opaque_ke::key_exchange::tripledh::TripleDH;
    type Hash = sha2::Sha512;
    type SlowHash = ScryptParams;
}

#[pymodule]
fn opaquepy(py: Python<'_>, m: &PyModule) -> PyResult<()> {
    let opqrust = PyModule::new(py, "_opqrust")?;
    opqrust.add_function(wrap_pyfunction!(generate_keys_py, opqrust)?)?;
    opqrust.add_function(wrap_pyfunction!(register_server_py, opqrust)?)?;
    opqrust.add_function(wrap_pyfunction!(register_server_finish_py, opqrust)?)?;
    opqrust.add_function(wrap_pyfunction!(login_server_py, opqrust)?)?;
    opqrust.add_function(wrap_pyfunction!(login_server_finish_py, opqrust)?)?;

    m.add_submodule(opqrust)?;

    Ok(())
}

#[pyfunction]
fn generate_keys_py() -> (String, String) {
    let keypair = generate();
    let private_key = keypair.private().to_vec();
    let public_key = keypair.public().to_vec();

    let private_encoded = base64::encode_config(private_key, base64::URL_SAFE);
    let public_encoded = base64::encode_config(public_key, base64::URL_SAFE);

    (private_encoded, public_encoded)
}

trait ToPyErr {
    fn to_pyerr(self) -> PyErr;
}

impl ToPyErr for ProtocolError {
    fn to_pyerr(self) -> PyErr {
        PyValueError::new_err(format!("{:?}", self))
    }
}

impl ToPyErr for PakeError {
    fn to_pyerr(self) -> PyErr {
        PyValueError::new_err(format!("{:?}", self))
    }
}

impl ToPyErr for DecodeError {
    fn to_pyerr(self) -> PyErr {
        PyValueError::new_err(self.to_string())
    }
}

#[pyfunction]
fn register_server_py(client_request: String, public_key: String) -> PyResult<(String, String)> {
    let request_bytes = base64::decode_config(client_request, base64::URL_SAFE)
        .map_err(ToPyErr::to_pyerr)?;
    let client_request: RegistrationRequest<DefaultCipher> = RegistrationRequest::deserialize(&request_bytes)
        .map_err(ToPyErr::to_pyerr)?;
    let key_bytes = base64::decode_config(public_key, base64::URL_SAFE)
        .map_err(ToPyErr::to_pyerr)?;
    let public_key = Key::from_bytes(&key_bytes)
        .map_err(ToPyErr::to_pyerr)?;

    let s = server_register(client_request, &public_key)
        .map_err(ToPyErr::to_pyerr)?;

    let response_bytes = s.message.serialize();
    let state_bytes = s.state.serialize();

    let response_encoded = base64::encode_config(response_bytes, base64::URL_SAFE);
    let state_encoded = base64::encode_config(state_bytes, base64::URL_SAFE);

    Ok((response_encoded, state_encoded))
}

#[pyfunction]
fn register_server_finish_py(client_request_finish: String, registration_state: String) -> PyResult<String> {
    let request_bytes = base64::decode_config(client_request_finish, base64::URL_SAFE)
        .map_err(ToPyErr::to_pyerr)?;
    let client_request_finish: RegistrationUpload<DefaultCipher> = RegistrationUpload::deserialize(&request_bytes)
        .map_err(ToPyErr::to_pyerr)?;

    let state_bytes = base64::decode_config(registration_state, base64::URL_SAFE)
        .map_err(ToPyErr::to_pyerr)?;
    let registration_state: ServerRegistration<DefaultCipher> = ServerRegistration::deserialize(&state_bytes)
        .map_err(ToPyErr::to_pyerr)?;

    let s = server_register_finish(client_request_finish, registration_state)
        .map_err(ToPyErr::to_pyerr)?;

    let password_file_bytes = s.serialize();

    let password_file_encoded = base64::encode_config(password_file_bytes, base64::URL_SAFE);

    Ok(password_file_encoded)
}

#[pyfunction]
fn login_server_py(password_file: String, client_request: String, private_key: String) -> PyResult<(String, String)> {
    let password_file_bytes = base64::decode_config(password_file, base64::URL_SAFE)
        .map_err(ToPyErr::to_pyerr)?;
    let password_file= ServerRegistration::<DefaultCipher>::deserialize(&password_file_bytes)
        .map_err(ToPyErr::to_pyerr)?;

    let request_bytes = base64::decode_config(client_request, base64::URL_SAFE)
        .map_err(ToPyErr::to_pyerr)?;
    let client_request: CredentialRequest<DefaultCipher> = CredentialRequest::deserialize(&request_bytes)
        .map_err(ToPyErr::to_pyerr)?;

    let key_bytes = base64::decode_config(private_key, base64::URL_SAFE)
        .map_err(ToPyErr::to_pyerr)?;
    let private_key = Key::from_bytes(&key_bytes)
        .map_err(ToPyErr::to_pyerr)?;

    let s = server_login(password_file, &private_key, client_request)
        .map_err(ToPyErr::to_pyerr)?;

    let response_bytes = s.message.serialize()
        .map_err(ToPyErr::to_pyerr)?;
    let state_bytes = s.state.serialize()
        .map_err(ToPyErr::to_pyerr)?;

    let response_encoded = base64::encode_config(response_bytes, base64::URL_SAFE);
    let state_encoded = base64::encode_config(state_bytes, base64::URL_SAFE);

    Ok((response_encoded, state_encoded))
}

#[pyfunction]
fn login_server_finish_py(client_request_finish: String, login_state: String) -> PyResult<String> {
    let request_bytes = base64::decode_config(client_request_finish, base64::URL_SAFE)
        .map_err(ToPyErr::to_pyerr)?;
    let client_request_finish: CredentialFinalization<DefaultCipher> = CredentialFinalization::deserialize(&request_bytes)
        .map_err(ToPyErr::to_pyerr)?;

    let state_bytes = base64::decode_config(login_state, base64::URL_SAFE)
        .map_err(ToPyErr::to_pyerr)?;
    let login_state: ServerLogin<DefaultCipher> = ServerLogin::deserialize(&state_bytes)
        .map_err(ToPyErr::to_pyerr)?;

    let s = server_login_finish(client_request_finish, login_state)
        .map_err(ToPyErr::to_pyerr)?;

    let session_key_bytes = s.session_key;

    let session_key_encoded = base64::encode_config(session_key_bytes, base64::URL_SAFE);

    Ok(session_key_encoded)
}

fn generate() -> KeyPair<RistrettoPoint> {
    let mut rng = OsRng;
    DefaultCipher::generate_random_keypair(&mut rng)
}

fn server_register(client_request: RegistrationRequest<DefaultCipher>, public_key: &Key) -> Result<ServerRegistrationStartResult<DefaultCipher>, ProtocolError> {

    let mut server_rng = OsRng;
    ServerRegistration::<DefaultCipher>::start(
        &mut server_rng,
        client_request,
        public_key,
    )
}

fn server_register_finish(client_request_finish: RegistrationUpload<DefaultCipher>, registration_state: ServerRegistration<DefaultCipher>)
    -> Result<ServerRegistration<DefaultCipher>, ProtocolError> {

    registration_state.finish(
        client_request_finish
    )
}

fn server_login(password_file: ServerRegistration<DefaultCipher>, private_key: &Key, client_request: CredentialRequest<DefaultCipher>)
    -> Result<ServerLoginStartResult<DefaultCipher>, ProtocolError> {

    let mut server_rng = OsRng;
    ServerLogin::start(
        &mut server_rng,
        password_file,
        private_key,
        client_request,
        ServerLoginStartParameters::default(),
    )
}

fn server_login_finish(client_request_finish: CredentialFinalization<DefaultCipher>, login_state: ServerLogin<DefaultCipher>)
    -> Result<ServerLoginFinishResult<DefaultCipher>, ProtocolError> {
    login_state.finish(
        client_request_finish
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn gen_test() {
        generate();
    }

    #[test]
    fn server_register() {
        // let x = generate();
        // let pub_string = base64::encode_config(x.public().as_slice(), base64::URL_SAFE);
        // let priv_string = base64::encode_config(x.private().as_slice(), base64::URL_SAFE);
        // println!("{}", pub_string);
        // println!("{}", priv_string);

        //password 'abc'
        let message = "HOqqdRYhiUDCYdEFt224RopWkUyh_bpAOulzXDk7CQc=".to_string();
        let pub_string = "yUY5svc-Tb2xp02m60Lut1p0aI0mJoUzefL1vKrnDgk=".to_string();
        //let pub_string = "_HIpSdpN8JQcSObRvmj1f_lTTKIrdwRVCvvMzunGKXQ=".to_string();
        let (response, state) = register_server_py(message, pub_string).unwrap();
        println!("{}", response);
        println!("{}", state);
    }

    #[test]
    fn server_register_finish() {
        let client_message = "rBnW8cAcnETa5TOIIR8OCByNsphJwLxqKK6a27NWxFsBE6zKiPEk3j9mpD-KgJkPAOZwBbIViVKVNzX8546lxUxTzEESQGlfRmvsZw1F3eyk5FtfIEHqCP0FlzfcYGGhSR7GE1TmF6FipKDsGx37q5fbTXrMuw4YDpxbwR-68R9_ot13JeJT7h7RRZYDQi8EeK9VdMB_bRUhgt9C5l6WTgQ=".to_string();
        let server_state = "KrpCip-KvRxxIbw5zT67he-yaKLKA42-ZbD-VHzYBQE=".to_string();
        let password_file = register_server_finish_py(client_message, server_state).unwrap();
        println!("{}", password_file)

        // example file:
        // KrpCip-KvRxxIbw5zT67he-yaKLKA42-ZbD-VHzYBQGsGdbxwBycRNrlM4ghHw4IHI2ymEnAvGoorprbs1bEWwETrMqI8STeP2akP4qAmQ8A5nAFshWJUpU3NfznjqXFTFPMQRJAaV9Ga-xnDUXd7KTkW18gQeoI_QWXN9xgYaFJHsYTVOYXoWKkoOwbHfurl9tNesy7DhgOnFvBH7rxH3-i3Xcl4lPuHtFFlgNCLwR4r1V0wH9tFSGC30LmXpZOBA==
    }

    #[test]
    fn server_login() {
        let client_message = "jFeU2zdhMoz_h6r5OveE4zlM7U5lNoCAjsNhAhXiuFf4Sia6sILBzDdyiN9sG509LpoXRjLEllhuOAPwAFOKAgAAxonvu5GIwabnS4Xr9UQVyEWUqbC8qGGJRSxGFmFGXV8=".to_string();
        // password 'abc'
        let password_file = "KrpCip-KvRxxIbw5zT67he-yaKLKA42-ZbD-VHzYBQGsGdbxwBycRNrlM4ghHw4IHI2ymEnAvGoorprbs1bEWwETrMqI8STeP2akP4qAmQ8A5nAFshWJUpU3NfznjqXFTFPMQRJAaV9Ga-xnDUXd7KTkW18gQeoI_QWXN9xgYaFJHsYTVOYXoWKkoOwbHfurl9tNesy7DhgOnFvBH7rxH3-i3Xcl4lPuHtFFlgNCLwR4r1V0wH9tFSGC30LmXpZOBA==".to_string();
        let private_key = "Xev6fnTEs9xtQq8I8RgnXXld88howDq30w7iDU3FhwI=".to_string();

        let (response, state) = login_server_py(password_file, client_message, private_key).unwrap();

        println!("{}", response);
        println!("{}", state);
    }

    #[test]
    fn server_login_finish() {
        // correspond to above
        let client_message = "CpvOy9cd_znwySMLqxEobK1lxW3AQjTm13WZqS-HokE2pfsgmLpa4Te37D6etikLJZoqBdHW2t9QzxC9tyId8A==".to_string();
        let state = "eOrS1I-u-0SdGYjXTInhLDKuWLXM_e0cAzHTCTRsdS40-DBAHcD9UMEaARoLuqaVuQgGoJL1_hVQ8e65M9WxqGa8hie68tXuO9cCU_HdubeZwITsvJk9edOngauLzx_rMD9Np5mVryvUCxDrV3TNh7Eux3O3j88cbnWbir-mjZZDM7QxblKMP34ZBflxqmHxMj5aEJc3mSUsknp2RM1LedK9mrXpySX9kft6t_GhN1Hwz7wYqP4A-sEMrpuvB8ms".to_string();

        let session = login_server_finish_py(client_message, state).unwrap();

        println!("{}", session)
    }
}