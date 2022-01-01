from random import randint


# правила игры
RULES = 'Answer "yes" if the number is prime. Otherwise answer "no".'


# проверка, что число простое
def is_prime(number):
    divisor = 2
    while divisor ** 2 <= number and (number
                                      % divisor != 0):
        divisor += 1
    return (divisor ** 2) > number


# определяем правильный ответ
def get_games_data():

    question = randint(1, 99)

    if is_prime(question) is True:
        answer = 'yes'
    else:
        answer = 'no'

    return [str(question), str(answer)]
