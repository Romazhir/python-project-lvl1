from random import randint


# правила игры
def rules_prime():
    return 'Answer "yes" if the number is prime. Otherwise answer "no".'


# число для вопроса и игры
def get_prime_question_number():
    return randint(1, 99)


# проверка, что число простое
def is_prime(number):
    divisor = 2
    while divisor ** 2 <= number and (number
                                      % divisor != 0):
        divisor += 1
    return (divisor ** 2) > number


# определяем правильный ответ
def get_prime_right_answer(question_string):
    if is_prime(question_string) is True:
        return 'yes'
    else:
        return 'no'
