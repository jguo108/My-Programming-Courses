

score = 0
print("Welcome to the Animal Quiz!")


# print(answer)
# print(answer == "cheetah")


def check_answer(correct_answer):
    global score
    # if answer.lower() == "cheetah":
    if answer.lower() == correct_answer:
        print("Awesome! You got it right!")
        score = score + 1
    # print("The first question is pretty simple, huh?")
    else:
        # print("Oops! The answer should be cheetah!")
        print("Oops! The answer should be ", correct_answer)
    # check_answer(answer=answer1, guess="cheetah")


answer = input("Which is the fastest land animal?")
# check_answer()
check_answer('cheetah')

print("Your score is:", score)
