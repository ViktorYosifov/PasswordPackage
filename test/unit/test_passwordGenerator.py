import unittest
from passman.helper.passwordGenerator import Generator
import string

class TestGenerator(unittest.TestCase):

    def test_generate_password_low_complexity(self):
        generator = Generator()
        password = generator.generate_password(10, "low")

        self.assertEqual(len(password), 10)
        self.assertTrue(all(c in string.ascii_letters + string.digits for c in password))

    def test_generate_password_medium_complexity(self):
        generator = Generator()
        password = generator.generate_password(15, "medium")

        self.assertEqual(len(password), 15)
        self.assertTrue(all(c in string.ascii_letters + string.digits + string.punctuation for c in password))

    def test_generate_password_high_complexity(self):
        generator = Generator()
        password = generator.generate_password(20, "high")

        self.assertEqual(len(password), 20)
        self.assertTrue(
            all(c in string.ascii_letters + string.digits + string.punctuation + string.whitespace for c in password))

    def test_invalid_complexity(self):
        generator = Generator()
        with self.assertRaises(ValueError):
            generator.generate_password(12, "invalid_complexity")

    def test_negative_length(self):
        generator = Generator()
        with self.assertRaises(ValueError):
            generator.generate_password(-5, "low")


if __name__ == '__main__':
    unittest.main()