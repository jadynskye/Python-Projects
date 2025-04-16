#Password Generator Project

import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
           ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
           '`', '~', '!', '@', '#', '$', '%', '^', '&', '*',
           '(', ')', '-', '_', '=', '+', '[', ']', '{', '}']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]

#To center the inital message 
intro = "Welcome to my password generator! "

print("*" * 50)
print(intro.center(50, " "))
print("*" * 50)

#User inputs
user_letters = int(input("\nHow many letter would you like your password? "))
user_symbols = int(input("\nHow many symbols would you like your password? "))
user_numbers = int(input("\nHow many numbers would you like your password? "))

password = ''

for let in range(0, user_letters):
    random_letter = random.choice(letters)
    password += random_letter

for symb in range(0,user_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol 

for num in range(0, user_numbers):
    random_number = random.choice(numbers)
    password += random_number

#converting the string to a list
list_password = password.split()

#shuffling the password 
random.shuffle(list_password)

#converting the password back to a string for the user
final_password = " ".join(list_password)

print()
print("*" * 50)
print(f"\nYour password is : {final_password}\n")
