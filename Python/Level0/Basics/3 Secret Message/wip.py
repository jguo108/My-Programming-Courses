
'''
def print_character(character):
    # print(message[0])
    print(character)
'''


def encrypt_character(character):
    print(character)


alphabet = 'abcdefghijklmnopqrstuvwxyz'

message = input('Enter a message: ')
key = int(input('Enter a key: '))
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
    encrypt_character(character)
