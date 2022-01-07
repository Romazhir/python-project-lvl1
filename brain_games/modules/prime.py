from random import randint


RULE = 'Answer "yes" if the number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
            return False
    for divisor in range(2, number // 2 + 1):
        if divisor < number and number % divisor == 0:
            return False
    else:
        return True


def generate_question_answer():
    question = randint(1, 99)

    if is_prime(question) is True:
        answer = 'yes'
    else:
        answer = 'no'

    return (str(question), answer)
