import art
import os

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def program_menu():
    user_choice = int(input("This program encrypt or decrypt a message using the Caesar Cipher\n"
                            "Type what you want to do:\n"
                            "0 - To encrypt a message\n"
                            "1 - To decrypt a message\n"))
    return user_choice

def letter_index_checker(letter, shift_number, function):
    letter_index = ALPHABET.index(letter)
    if function == "encode":
        if (letter_index + shift_number) >= len(ALPHABET):
            letter_index_shifted = (letter_index + shift_number) % len(ALPHABET)
        else:
            letter_index_shifted = letter_index + shift_number
    else:
        negative_index_length = (-(len(ALPHABET)))
        if (letter_index - shift_number) < negative_index_length:
            letter_index_shifted = (letter_index - shift_number) % negative_index_length
        else:
            letter_index_shifted = letter_index - shift_number
    return letter_index_shifted

def encrypt(message, shift_number, function):
    encrypted_message = ""
    for letter in message:
        if letter in ALPHABET:
            shift_letter_index = letter_index_checker(letter, shift_number, function)
            encrypted_message += ALPHABET[shift_letter_index]
        else:
            encrypted_message += letter
    return encrypted_message

def decrypt(message, shift_number, function):
    decrypted_message = ""
    for letter in message:
        if letter in ALPHABET:
            shift_letter_index = letter_index_checker(letter, shift_number, function)
            decrypted_message += ALPHABET[shift_letter_index]
        else:
            decrypted_message += letter
    return decrypted_message

keep_program_running = True
while keep_program_running == True:
    print(art.logo)
    menu = program_menu()
    if menu != 0 and menu != 1:
        print("This option isn't valid, choose one of the listed options.")
    elif menu == 0:
        function = "encode"
        message = input("Type your message: ").lower()
        shift_number = int(input("Type the shift number: "))
        encrypted_message = encrypt(message, shift_number, function)
        print(f"Here's the encrypted message: {encrypted_message}.")
    else:
        function = "decode"
        message = input("Type your message: ").lower()
        shift_number = int(input("Type the shift number: "))
        decrypted_message = decrypt(message, shift_number, function)
        print(f"Here's the decrypted message: {decrypted_message}")

    user_choice = input("Do you want to encrypt or decrypt another message? "
                        "Type 'yes' if you want, otherwise type 'no'.\n")
    os.system("clear")
    if user_choice == 'no':
        keep_program_running = False