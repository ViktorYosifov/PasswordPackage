from passman.helper.Decryptor import Decryptor
from passwordGenerator import Generator
from Encryptor import Encryptor

class Manager:
    """ 1.Takes user input for length and complexity of the password
        2.Shows the user his credentials
        3.Saves the user's credentials in a database, that is hidden"""

    def manage_all(self):

        length = int(input("Enter length for your password: "))
        print("Choose complexity level:\n1.low\n2.medium\n3.high")
        complexity = input("Enter complexity level: ")
        password_generator = Generator()
        password = password_generator.generate_password(length, complexity)

        encryptor = Encryptor()
        encrypted_password = encryptor.encrypt_password(password)

        filename = "database.txt"
        Encryptor.save_pass(encrypted_password, filename)

        decryptor = Decryptor(encryptor.key)
        decrypted_password = decryptor.decrypt_password(encrypted_password)

        loaded_encrypted_password = encryptor.load_pass(filename)
        decrypted_loaded_password = decryptor.decrypt_password(loaded_encrypted_password)











