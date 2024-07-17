# Notes:
# https://www.notion.so/3-Secret-Message-2bf1658130d44288b0aa2193f4eee184

def cipher(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[key:] + alphabet[:key]

    # Create empty string to store encoded message
    new_message = ''

    # Loop through each character in the message
    for char in message:
        if char.isalpha():  # Check if character is a letter
            # Find the index of the character in the alphabet
            index = alphabet.find(char.lower())
            # Get the shifted character from the shifted alphabet
            new_char = shifted_alphabet[index]
            # Preserve uppercase/lowercase
            if char.isupper():
                new_message += new_char.upper()
            else:
                new_message += new_char
        else:
            # Keep non-alphabetic characters the same
            new_message += char

    return new_message


# Get message and shift value from user
option = int(input('Do you want to encrypt(1) or decrypt(2)? '))

if option == 1:
    # Encode
    message = input('Enter a message: ')
    key = int(input('Enter a key: '))
    message = cipher(message, key)
    print('Encoded message: ', message)
elif option == 2:
    # Decode
    message = input('Enter your message: ')
    key = int(input('Enter a key: '))
    message = cipher(message, -key)
    print('Decoded message: ', message)
else:
    print('Invalid option')
