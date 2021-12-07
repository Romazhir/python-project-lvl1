import prompt
from random import randint


# узнаем имя игрока
def get_user_name():
    return prompt.string('May I have your name? ')

# user_name = get_user_name()


# задаем число для игры
def get_question_number():
    return randint(1, 999)

# print(get_question_number())


# Определяем правильный ответ, исходя из числа для игры
def get_right_answer(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'

# test_number = randint(1,999)
# print(test_number)
# print(get_right_answer(test_number))


# Получаем ответ игрока
def get_user_answer():
    return input('Your answer: ')

# test_user_answer = get_user_answer()


# Сравниваем ответ игрока с правильным ответом
def get_game_result(arg_right_answer, arg_user_answer):
    if arg_user_answer == arg_right_answer:
        return True
    else:
        return False

# print(get_game_result(get_right_answer(test_number),test_user_answer))
