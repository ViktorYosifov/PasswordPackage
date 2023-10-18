from cryptography.fernet import Fernet

class Decryptor:

    def __init__(self, key):
        self.key = key

    def decrypt_password(self, encrypted_password):
        cipher_suite = Fernet(self.key)
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode('utf-8')
        return decrypted_password

    def load_pass(self, filename):
        with open(filename,'rb') as file:
            encrypted_password = file.read()
        return encrypted_password