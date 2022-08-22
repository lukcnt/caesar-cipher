import art

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def menu_of_the_program():
    user_choice = int(input("This program encrypt or decrypt a message using the Caesar Cipher\n"
                            "Type what you want to do:\n"
                            "0 - To encrypt a message\n"
                            "1 - To decrypt a message\n"))
    return user_choice

print(art.logo)
menu = menu_of_the_program()
if menu != 0 and menu != 1:
    print("This option isn't valid, choose one of the listed options.")
elif menu == 0:
    print("Encrypt")
else:
    print("Decrypt")