# Notes:
# https://www.notion.so/5-Guess-the-Word-1e5af5c3f4c44fd7a386c5a513253e93

from random import *


def update_partial_word(guessed_letter, secret_word, partial_word):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            partial_word[index] = guessed_letter
        index = index + 1


words = ["pizza", "fairy", "teeth", "shirt", "otter", "plane"]
# words = []
# file = open('words.txt', 'r')
# words = file.read().splitlines()

# short cut to create a list of charaters
partial_word = list(5 * '*')
# partial_word = list('*****')
# partial_word = ['*','*','*','*','*']

guessed_correctly = False
attempts_left = 9

# use 'choice' to choose a random item from a list
secret_word = choice(words)
print("Secret word is: '{secret_word}'")

while attempts_left > 0 and not guessed_correctly:
    print(" ".join(partial_word))
    print("Attempts left: {attempts_left}")
    guess = input("Guess a letter or the whole word: ")

    if guess == secret_word:
        guessed_correctly = True
    elif guess in secret_word:
        update_partial_word(guess, secret_word, partial_word)
    else:
        print("Opoos! You guessed it wrong!")
        attempts_left = attempts_left - 1

if guessed_correctly:
    print(f"You won! The secret word was '{secret_word}'")
    # print('You won! The secret word was ' + secret_word)
else:
    print(f"You lost! The secret word was '{secret_word}'")
    # print('You lost! The secret word was ' + secret_word)
