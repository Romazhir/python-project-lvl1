# функции для brain-calc

from random import randint
from random import choice


# правила игры
def rules_calc():
    return 'What is the result of the expression?'


# случайное число
def get_calc_question_number():
    return randint(1, 99)


# определение символа оператора
def get_calc_operator_symbol():
    operations = ['+', '-', '*']
    return choice(operations)


# строка для вопроса
def get_calc_question_expression():
    return '{} {} {}'.format(get_calc_question_number(),
                             get_calc_operator_symbol(),
                             get_calc_question_number())


# определение правильного ответа
def get_calc_right_answer(expression):
    return str(eval(expression))
