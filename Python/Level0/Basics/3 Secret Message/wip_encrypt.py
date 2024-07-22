
'''
def print_character(character):
    # print(message[0])
    print(character)
'''

'''
def encrypt_character(character):
    index = alphabet.find(character)
    new_index = index + key
    new_character = alphabet[new_index]
    # print(character)
    # print(index)
    # print(new_index)
    # print(new_character)
    return new_character
'''

'''
def encrypt_character(character):
    lower_character = character.lower()
    index = alphabet.find(lower_character)
    new_index = index + key
    new_character = alphabet[new_index]
    return new_character
'''

'''
def encrypt_character(character):
    lower_character = character.lower()
    index = alphabet.find(lower_character)
    new_index = index + key
    new_character = alphabet[new_index]
    if character.isupper():
        new_character = new_character.upper()
        return new_character
    else:
        return new_character
'''


def encrypt_character(character):
    if character.isalpha():
        lower_character = character.lower()
        index = alphabet.find(lower_character)
        new_index = index + key
        # new_character = alphabet[new_index]
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
# print(message)
# print(key)

# print(message[0])
# print(message[1])
# print(message[2])
# print(message[3])
# print(message[4])

# print_character(message[0])
# print_character(message[1])
# print_character(message[2])
# print_character(message[3])
# print_character(message[4])

# for i in range(len(message)):
#    print_character(message[i])

# for character in message:
#    print_character(character)

for character in message:
    # encrypt_character(character)
    new_character = encrypt_character(character)
    # new_message + new_character
    # new_message = new_message + new_character
    new_message += new_character
    # print(new_character)

print("The encrypted message is:", new_message)
