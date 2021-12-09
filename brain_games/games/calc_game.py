# функции для brain-calc

import operator
from random import choice


# случайный выбор оператора
def get_calc_operator():
    operator_list = [operator.add, operator.sub, operator.mul]
    return choice(operator_list)

# print(get_calc_operator()(1,2))


# определение символа оператора
def get_calc_operator_symbol(calc_operator):
    if calc_operator == operator.add:
        return '+'

    if calc_operator == operator.sub:
        return '-'

    if calc_operator == operator.mul:
        return '*'

# calc_operator = get_calc_operator()
# print(calc_operator(2,3))
# print(get_calc_operator_symbol(calc_operator))


# определение правильного ответа
def get_calc_right_answer(num1, num2, calc_operator):
    return calc_operator(num1, num2)

# print(get_calc_right_answer(2, 3, calc_operator))
