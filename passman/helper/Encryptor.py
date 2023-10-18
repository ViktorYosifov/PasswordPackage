from cryptography.fernet import Fernet

class Encryptor:

    def __init__(self, key = None):
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key

    def encrypt_password(self, password):

        cipher_suite = Fernet(self.key)
        encrypted_password = cipher_suite.encrypt(password.encode('utf-8'))
        return encrypted_password

    def save_pass(self, encrypted_password, filename):
        with open(filename, 'wb') as file:
            file.write(encrypted_password)

