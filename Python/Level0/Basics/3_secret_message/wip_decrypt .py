
'''
def encrypt_character(character):
    if character.isalpha():
        lower_character = character.lower()
        index = alphabet.find(lower_character)
        new_index = index + key
        new_character = alphabet[new_index % 26]
        if character.isupper():
            new_character = new_character.upper()
            return new_character
        else:
            return new_character
    else:
        return character


def decrypt_character(character):
    if character.isalpha():
        lower_character = character.lower()
        index = alphabet.find(lower_character)
        new_index = index - key
        new_character = alphabet[new_index % 26]
        if character.isupper():
            new_character = new_character.upper()
            return new_character
        else:
            return new_character
    else:
        return character
'''


def convert_character(character, key):
    if character.isalpha():
        lower_character = character.lower()
        index = alphabet.find(lower_character)
        new_index = index + key
        new_character = alphabet[new_index % 26]
        if character.isupper():
            new_character = new_character.upper()
            return new_character
        else:
            return new_character
    else:
        return character


alphabet = "abcdefghijklmnopqrstuvwxyz"
new_message = ""

message = input("Enter a message: ")
key = int(input("Enter a key: "))

choice = input("Do you want to encrypt or decrypt?")

if choice == "encrypt":
    for character in message:
        # new_character = encrypt_character(character)
        new_character = convert_character(character, key)
        new_message += new_character
    print("The encrypted message is:", new_message)
# else:
#    print("The decrypted message is:", message)
elif choice == "decrypt":
    for character in message:
        # new_character = decrypt_character(character)
        new_character = convert_character(character, -key)
        new_message += new_character
    print("The decrypted message is:", new_message)
else:
    print("Invalid choice.")
