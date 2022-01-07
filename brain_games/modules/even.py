from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return (number % 2) == 0


def generate_question_answer():
    question = randint(1, 99)

    if is_even(question) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return (str(question), answer)
