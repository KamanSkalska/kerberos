from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
def derive_key_from_password(password):
    # Using PBKDF2 for key derivation
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256 requires a 256-bit key
        salt=b"salty_salt",
        iterations=100000,  # Adjust the number of iterations based on your security requirements
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_message(message, key):
    # Using AES encryption in CBC mode
    iv = b'1234567890123456'  # Initialization Vector, should be random and unique for each encryption
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    return ciphertext