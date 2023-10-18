import random
import string


class Generator:

    def generate_password(self, length, complexity):

        if complexity == "low":
            temp = string.ascii_letters + string.digits
        elif complexity == "medium":
            temp = string.ascii_letters + string.digits + string.punctuation
        elif complexity == "high":
            temp = string.ascii_letters + string.digits + string.punctuation + string.whitespace
        else:
            raise ValueError("Invalid complexity level")

        if length <= 0:

            raise ValueError("Password must be longer")

        password = ''.join(random.choice(temp) for _ in range(length))

        return password








