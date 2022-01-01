from random import randint


# правила игры
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


# проверка числа на четность
def is_even(number):
    return (number % 2) == 0


# формирование вопроса и вычисление правильного ответа
def get_games_data():

    question = randint(1, 99)

    if is_even(question) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return [str(question), str(right_answer)]
