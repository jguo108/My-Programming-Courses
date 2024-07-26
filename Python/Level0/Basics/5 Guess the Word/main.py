# Notes:
# https://www.notion.so/5-Guess-the-Word-1e5af5c3f4c44fd7a386c5a513253e93

from random import *


def update_answer(guessed, secret_word, answer):
    index = 0
    while index < len(secret_word):
        if guessed == secret_word[index]:
            answer[index] = guessed
        index += 1


words = ["pizza", "fairy", "teeth", "shirt", "otter", "plane"]
# words = []
# file = open('words.txt', 'r')
# words = file.read().splitlines()

# short cut to create a list of charaters
answer = list(5 * '*')
# answer = list('*****')
# answer = ['*','*','*','*','*']

bingo = False
attempts_left = 9

# use 'choice' to choose a random item from a list
secret_word = choice(words)
print(f"The secret word is: {secret_word}")

while attempts_left > 0 and not bingo:
    print(" ".join(answer))
    print(f"Attempts left: {attempts_left}")
    guess = input("Guess a letter or the whole word: ")

    if guess == secret_word:
        bingo = True
    elif guess in secret_word:
        update_answer(guess, secret_word, answer)
    else:
        print("Oops! You guessed it wrong! Try again.")
        attempts_left -= 1

if bingo:
    print(f"You won! The secret word was: {secret_word}")
    # print('You won! The secret word was ' + secret_word)
else:
    print(f"You lost! The secret word was: {secret_word}")
    # print('You lost! The secret word was ' + secret_word)
