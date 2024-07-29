from random import *


words = ["pizza", "teeth", "shirt", "plane", "grass"]
secret_word = choice(words)

# print("The secret word is:", secret_word)
print(f"The secrect word is: {secret_word}")

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

    if len(guess) == 1 secret_word.find(guess):
        pass
    # if len(guess) == 1 and secret_word.find(guess)


print("End of game")
