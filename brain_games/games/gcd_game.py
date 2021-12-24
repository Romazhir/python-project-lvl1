# функции для brain-gcd

from random import randint


# правила игры
def rules_gcd():
    return 'Find the greatest common divisor of given numbers.'


# случайное число
def get_gcd_question_number():
    return randint(1, 99)


# строка для вопроса
def get_gcd_question_string():
    return '{} {}'.format(get_gcd_question_number(),
                          get_gcd_question_number())


# определяем правильный ответ (перевод в str можно перенести в движок)
def get_gcd_right_answer(questions_string):
    numbers_list = questions_string.split(' ')

    first_number = int(numbers_list[0])
    second_number = int(numbers_list[1])

    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number

    return first_number
