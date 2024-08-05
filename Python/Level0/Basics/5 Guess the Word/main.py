from random import *


file = open("5 Guess the Word/words.txt", "r")
content = file.read()
file.close()

words = content.splitlines()
secret_word = choice(words)
answer = ["*", "*", "*", "*", "*"]

attempts_left = 9

while True:
    print(" ".join(answer))
    print(f"Attempts left: {attempts_left}")
    guess = input("Guess a letter or the whole word: ")

    if len(guess) == 1 and secret_word.find(guess) != -1:
        # pass
        print("Guess is a single character in secret word")
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                answer[index] = guess
    elif guess == secret_word:
        print(f"You won! The secret word was: {secret_word}")
        break
    else:
        attempts_left -= 1
        if attempts_left == 0:
            print(f"You lost! The secret word was: {secret_word}")
            break
        else:
            print("Oops! You guessed it wrong! Try again.")
