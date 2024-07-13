# Notes:
# https://www.notion.so/3-Animal-Quiz-104d1092ae4f456ea81c5fbb201e1c11

score = 0


def check_answer(answer, guess):
    global score
    # KP: string comparison and "lower" function
    if guess.lower() == answer.lower().strip():
        print("Awesome! You got it right!")
        score = score + 1
    else:
        # KP: string concatenation
        print("Oops! The answer shoud be: " + answer)


print("Welcome to the Animal Quiz!")
answer1 = input("Which is the fastest land animal?")
# check_answer(answer1, "cheetah")
check_answer(answer=answer1, guess="cheetah")
answer2 = input("Which is the largest animal?")
# check_answer(answer2, "blue whale")
check_answer(answer=answer2, guess="blue whale")
answer3 = input("Which land animal can't jump?")
# check_answer(answer3, "elephant")
check_answer(answer=answer3, guess="elephant")

# print("Your score is ", score)
print("Your score is " + str(score))  # KP: convert number to string
