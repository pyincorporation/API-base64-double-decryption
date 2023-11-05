import base64
from cryptography.fernet import Fernet
import os

# Access settings variables
# sec_key = settings.SECRET_KEY

# settings.py
def generate_fernet_key():
    return base64.urlsafe_b64encode(os.urandom(32))

sec_key = generate_fernet_key()

def encrypt_data(data):
    cipher_suite = Fernet(sec_key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return base64.b64encode(encrypted_data).decode()

def decrypt_data(encrypted_data):
    cipher_suite = Fernet(sec_key)
    decoded_data = base64.urlsafe_b64decode(encrypted_data.encode())
    decrypted_data = cipher_suite.decrypt(decoded_data)
    return decrypted_data.decode()