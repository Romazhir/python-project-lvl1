from random import randint


# правила игры
def rules_even():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


# число для вопроса и игры
def get_question_number():
    return randint(1, 99)


# проверка числа на четность
def is_even(number):
    return (number % 2) == 0


# определение правильного ответа
def get_even_right_answer(game_number):
    if is_even(game_number) is True:
        return 'yes'
    else:
        return 'no'
