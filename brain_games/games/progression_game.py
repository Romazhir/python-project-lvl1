import random


# правила игры
RULES = 'What number is missing in the progression?'

FINITE_NUMBER_INDEX = 9


# создаем арифметическую прогрессию
def make_arithmetic_progression():
    counter = 0
    progression_number = random.randint(1, 99)
    common_difference = random.randint(1, 99)
    progression_list = []

    while counter <= FINITE_NUMBER_INDEX:
        progression_list.append(progression_number)
        progression_number += common_difference
        counter += 1
    return progression_list


# формируем вопрос и правильный ответ
def get_games_data():
    progression_list = make_arithmetic_progression()
    hidden_element_index = random.randint(0, FINITE_NUMBER_INDEX)

    answer = progression_list.pop(hidden_element_index)

    progression_list.insert(hidden_element_index, '..')

    question = ' '.join(map(str, progression_list))

    return [str(question), str(answer)]
