# функции для brain_progression

import operator
import random


# формирование прогрессии для игры
# start_number = random.randint(1, 99)
# quantity_elements = 10
# progression_step = random.randint(1, 99)

def get_game_list(start_number, quantity_elements, progression_step):
    step_counter = 1
    number = start_number
    progression_list = []
    while step_counter <= quantity_elements:
        progression_list.append(number)
        number = operator.add(number, progression_step)
        step_counter += 1
    return progression_list

# game_list = get_game_list()
# print(game_list)


# определение индекса элемента, который будет скрыт
def get_hidden_element():
    return random.randint(0, 9)

# формирование прогрессии для показа игроку
# x_number = random.randint(0, 9)
# right_answer = game_list[x_number]


def get_game_list_for_player(hidden_element, game_list):
    element_counter = 0
    list_for_player = []
    while element_counter <= 9:
        if element_counter != hidden_element:
            list_for_player.append(game_list[element_counter])
        else:
            list_for_player.append('..')
        element_counter += 1
    return list_for_player

# game_list_for_player = get_game_list_for_player()
# print(*game_list_for_player, sep=' ')
# print(right_answer)
