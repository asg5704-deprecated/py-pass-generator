"""
Write a password generator in Python
Strong passwords have a mix of lowercase,
uppercase, numbers, and symbols.

Password should be random
"""
import sys
import string
import secrets
import random

# Function that prompts user for length
def ask_password_length():
    return input('How long do you want your password to be? ')

def run_program():
    print('Welcome to my password generator')
    answer = input('Would you like to generate a new password? ')
    
    answer = str(answer).lower()
    
    if answer == "yes" or answer == "y":
        print("Let's get started")
        start_password_process()
    else:
        sys.exit("Okay. Exiting...")


def start_password_process():
    pass_len = ask_password_length()
    
    while int(pass_len) < 7:
        print('%s characters long might be an easier password to break.' % str(pass_len))
        pass_len = ask_password_length()

    print('Cool so you want your password to be %s characters long.' % str(pass_len))
    print("Give me a minute while I create a password for you")

    #create_password(pass_len)
    create_secure_pass(pass_len)

"""
Non-secure password using random
def create_password(passwords_length):
    passwords_length = int(passwords_length)
    password_container = string.ascii_letters

    if passwords_length <= 12:
        password_container += string.digits
    else:
        password_container += string.digits + "!@#$%^&*()<>:\/.,+=-_~`"

    print('.....')
    password = ""
    for i in range(0, passwords_length):
        password += password_container[int(random.uniform(0, len(password_container)))]

    print('Your new [non-secure] password is: \n' + str(password))
"""

def create_secure_pass(passwords_length):
    passwords_length = int(passwords_length)

    password_container = string.ascii_letters + string.digits + "!@#$%^&*()<>:\/.,+=-_~`"
    print(".....")
    password = ""
    for i in range(0, passwords_length):
        password += secrets.choice(password_container)

    print("Your new [secure] password is: \n" + str(password))
    
run_program()