import unittest
from passman.helper.Encryptor import Encryptor
from cryptography.fernet import Fernet
import os

class TestEncryptor(unittest.TestCase):
    def setUp(self):
        self.key = Fernet.generate_key()
        self.encryptor = Encryptor(self.key)

    def tearDown(self):
        self.key = None
        self.encryptor = None

    def test_encrypt_password(self):
        password = "MySecretPassword"
        encrypted_password = self.encryptor.encrypt_password(password)
        self.assertNotEqual(password, encrypted_password.decode('utf-8'))

    def test_save_and_load_pass(self):
        password = "MySecretPassword"
        encrypted_password = self.encryptor.encrypt_password(password)
        filename = "test_encrypted_password.txt"
        self.encryptor.save_pass(encrypted_password, filename)
        self.assertTrue(os.path.isfile(filename))
        loaded_encrypted_password = self.encryptor.load_pass(filename)
        self.assertEqual(encrypted_password, loaded_encrypted_password)
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()