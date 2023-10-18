from passwordGenerator import Generator

class Manager:
    """ 1.Takes user input for length and complexity of the password
        2.Shows the user his credentials
        3.Saves the user's credentials in a database, that is hidden"""

    def user_input(self):

        length = int(input("Enter length for your password: "))
        print("Choose complexity level:\n1.low\n2.medium\n3.high")
        complexity = input("Enter complexity level: ")

        password_generator = Generator()

        password = password_generator.generate_password(length, complexity)

        return password








