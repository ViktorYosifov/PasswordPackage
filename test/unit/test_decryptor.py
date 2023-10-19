import unittest
from passman.helper.Decryptor import Decryptor
from cryptography.fernet import Fernet
import os

class TestDecryptor(unittest.TestCase):

    def setUp(self):
        self.key = Fernet.generate_key()
        self.decryptor = Decryptor(self.key)
        self.password = "MySecretPassword"
        self.encrypted_password = Fernet(self.key).encrypt(self.password.encode('utf-8'))
        self.filename = "test_encrypted_password.txt"

        with open(self.filename, 'wb') as file:
            file.write(self.encrypted_password)

    def tearDown(self):
        self.key = None
        self.decryptor = None
        self.password = None
        self.encrypted_password = None

        if os.path.isfile(self.filename):
            os.remove(self.filename)

    def test_decrypt_password(self):
        decrypted_password = self.decryptor.decrypt_password(self.encrypted_password)
        self.assertEqual(decrypted_password, self.password)

    def test_load_pass(self):
        loaded_encrypted_password = self.decryptor.load_pass(self.filename)
        self.assertEqual(loaded_encrypted_password, self.encrypted_password)


if __name__ == '__main__':
    unittest.main()
