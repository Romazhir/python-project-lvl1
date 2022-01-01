from random import randint


# правила игры
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


# проверка числа на четность
def is_even(number):
    return (number % 2) == 0


# формирование данных для игры
def get_games_data():

    question_number = randint(1, 99)

    if is_even(question_number) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return [str(question_number), str(right_answer)]
