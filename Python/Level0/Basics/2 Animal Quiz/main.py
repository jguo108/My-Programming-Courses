# Notes:
# https://www.notion.so/3-Animal-Quiz-104d1092ae4f456ea81c5fbb201e1c11


score = 0


def check_answer(answer, guess):
    global score
    # KP: string comparison and 'lower' function
    if guess.lower() == answer.lower().strip():
        print('Correct answer!')
        score = score + 1
    else:
        # KP: string concatenation
        print('Wrong! This answer shoud be: ' + answer)


print('Guess the Animal!')
answer1 = input('Which bear lives at the North Pole?')
# check_answer(answer1, "polar bear")
check_answer(answer=answer1, guess='polar bear')
answer2 = input('Which is the fastest land animal?')
# check_answer(answer2, "cheetah")
check_answer(answer=answer2, guess='cheetah')
answer3 = input('Which is the largest animal?')
# check_answer(answer3, "blue whale")
check_answer(answer=answer3, guess='blue whale')

# print('Your score is ', score)
print('Your score is ' + str(score))  # KP: convert number to string
