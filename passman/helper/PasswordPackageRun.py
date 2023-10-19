from passManager import *

print("Welcome to our password manager!."
      "It will provide you a secure password with length and complexity of your choice."
      "Feel Safe!")

if __name__ == "__main__":
    client = Manager()
    client.manage_all()