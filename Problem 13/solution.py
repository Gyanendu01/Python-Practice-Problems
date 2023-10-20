import getpass
import re


# Function to Enter Password
def read_password():
    password = getpass.getpass(prompt="\tEnter Your Password(max 7 characters and combination of alphabets and numbers): ")
    return password

# Function to check the given condition and siplay the result
def check_password(password):
    if len(password) < 8:
        if re.match(r'^(?=.*[a-zA-Z])(?=.*\d).+$', password):
            print("\n\tGreat Your Password is {}".format(password))

    else:
        print("\n\tInvalid Password Please follow the instructions while providing your password")

# Main Program
val = read_password()
check_password(val)