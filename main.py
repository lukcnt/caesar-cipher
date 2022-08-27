import art

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def menu_of_the_program():
    user_choice = int(input("This program encrypt or decrypt a message using the Caesar Cipher\n"
                            "Type what you want to do:\n"
                            "0 - To encrypt a message\n"
                            "1 - To decrypt a message\n"))
    return user_choice

def index_checker(letter, shift_number):
    index_letter_encrypted = letter + shift_number
    if index_letter_encrypted >= len(ALPHABET):
        while index_letter_encrypted >= len(ALPHABET):
            index_letter_encrypted -= len(ALPHABET)
        return index_letter_encrypted
    elif index_letter_encrypted <= (-(len(ALPHABET))):
        while index_letter_encrypted <= (-(len(ALPHABET))):
            index_letter_encrypted += len(ALPHABET)
        return index_letter_encrypted
    else:
        return index_letter_encrypted

def encrypt(message, shift_number):
    encrypted_message = ""
    for letter in message:
        if letter in ALPHABET:
            index_shift_letter = index_checker(letter, shift_number)
            encrypted_message += ALPHABET[index_shift_letter]
        else:
            encrypted_message += letter
    return encrypted_message

print(art.logo)
menu = menu_of_the_program()
if menu != 0 and menu != 1:
    print("This option isn't valid, choose one of the listed options.")
elif menu == 0:
    message = input("Type your message: ").lower()
    shift_number = int(input("Type the shift number: "))
    encrypted_message = encrypt(message, shift_number)
    print(f"Here's the encrypted message: {encrypted_message}.")
else:
    print("Decrypt")