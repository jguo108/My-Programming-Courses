from random import *


file = open("5 Guess the Word/words.txt", "r")
content = file.read()
# print(content)
# lines = content.splitlines()
words = content.splitlines()
# print(lines)

# words = ["pizza", "teeth", "shirt", "plane", "grass"]


secret_word = choice(words)
# secret_word = "pizza"

# print("The secret word is:", secret_word)
# print(f"The secrect word is: {secret_word}")

# answer = "*****"
# answer = answer.replace("*", "n", 1)
# answer[3] = "n"
answer = ["*", "*", "*", "*", "*"]
# print(answer)
# print(" ".join(answer))

attempts_left = 9

while True:
    # pass
    print(" ".join(answer))
    print(f"Attempts left: {attempts_left}")
    guess = input("Guess a letter or the whole word: ")

    if len(guess) == 1 and secret_word.find(guess) != -1:
        # pass
        print("Guess is a single character in secret word")
        '''
        for character in secret_word:
            if character == guess:
                answer[secret_word.find(character)] = guess
        '''
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                answer[index] = guess
    elif guess == secret_word:
        print(f"You won! The secret word was: {secret_word}")
        break
    else:
        # print("Oops! You guessed it wrong! Try again.")
        # attempts_left = attempts_left - 1
        attempts_left -= 1
        if attempts_left == 0:
            print(f"You lost! The secret word was: {secret_word}")
            break
        else:
            print("Oops! You guessed it wrong! Try again.")


# print("End of game")
