from random import randint
from random import choice
import operator


RULE = 'What is the result of the expression?'
operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}


def generate_question_answer():
    number_1 = randint(1, 99)
    number_2 = randint(1, 99)
    symbol_operator = choice(list(operations.keys()))
    calc_operator = operations.get(symbol_operator)

    question = '{} {} {}'.format(number_1,
                                 symbol_operator,
                                 number_2)

    answer = calc_operator(number_1, number_2)

    return (question, str(answer))
