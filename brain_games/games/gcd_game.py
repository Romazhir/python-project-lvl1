from random import randint


# правила игры
RULES = 'Find the greatest common divisor of given numbers.'


# формирование вопроса и вычисление правильного ответа
def get_games_data():
    number_1 = randint(1, 99)
    number_2 = randint(1, 99)

    question = '{} {}'.format(number_1, number_2)

    answer = get_gcd(number_1, number_2)

    return [str(question), str(answer)]


# функция для вычисления НОД
def get_gcd(number_1, number_2):
    while number_1 != number_2:
        if number_1 > number_2:
            number_1 = number_1 - number_2
        else:
            number_2 = number_2 - number_1

    return number_1
