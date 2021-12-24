# функции для brain_progression

import random


FIRST_NUMBER_INDEX = 0
FINITE_NUMBER_INDEX = 9


# правила игры
def rules_progression():
    return 'What number is missing in the progression?'


# получаем первый элемент прогрессии
def get_first_progression_number():
    return random.randint(1, 99)


# получаем разность прогрессии
def get_common_difference():
    return random.randint(1, 99)


# получаем индекс скрытого элемента прогрессии
def get_hidden_index():
    return random.randint(FIRST_NUMBER_INDEX, FINITE_NUMBER_INDEX)


# создаем арифметическую прогрессию
def make_arithmetic_progression():
    counter = 0
    progression_number = get_first_progression_number()
    common_difference = get_common_difference()
    progression_list = []

    while counter <= FINITE_NUMBER_INDEX:
        progression_list.append(progression_number)
        progression_number += common_difference
        counter += 1
    return progression_list


# создаем прогрессию с пропущенным элементом
def make_progression_list_for_question():
    counter = 0
    hidden_index = get_hidden_index()
    progression_list = make_arithmetic_progression()
    list_for_question = []

    while counter <= FINITE_NUMBER_INDEX:
        if counter != hidden_index:
            list_for_question.append(progression_list[counter])
        else:
            list_for_question.append('..')
        counter += 1
    return list_for_question


# создаем строку для вопроса
def get_progression_question():
    return ' '.join(map(str, make_progression_list_for_question()))


# получаем правильный ответ
def get_progression_right_answer(question_string):
    question_string = list(question_string.split())

    if question_string.index('..') < (FINITE_NUMBER_INDEX - 2):
        common_difference = (int(question_string[
                             FINITE_NUMBER_INDEX]) - int(
                             question_string[FINITE_NUMBER_INDEX - 1]))
        progression_right_answer = (int(question_string[
                                    question_string.index('..') + 1
                                    ]) - common_difference)
    else:
        common_difference = (int(question_string[
                             FIRST_NUMBER_INDEX + 1]) - int(
                             question_string[FIRST_NUMBER_INDEX]))
        progression_right_answer = (int(question_string[
                                    question_string.index('..') - 1
                                    ]) + common_difference)
    return progression_right_answer
