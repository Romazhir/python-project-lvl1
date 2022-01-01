from random import randint
from random import choice
import operator


RULES = 'What is the result of the expression?'
operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}


# формирование вопроса и вычисление правильного ответа
def get_games_data():
    number_1 = randint(1, 99)
    number_2 = randint(1, 99)
    symbol_operator = choice(list(operators.keys()))
    calc_operator = operators.get(symbol_operator)

    question = '{} {} {}'.format(number_1,
                                 symbol_operator,
                                 number_2)

    answer = calc_operator(number_1, number_2)

    return [str(question), str(answer)]
