import random


RULES = 'What number is missing in the progression?'
ROUND_NUMBERS = 3
PROGRESSION_LENGTH = 10


def generate_progression(first, difference, length):
    progression = []

    for index in range(0, length):
        progression.append(first)
        first += difference
    return progression


def generate_question_answer():
    first_number = random.randint(1, 99)
    common_difference = random.randint(1, 99)
    hidden_element_index = random.randint(0, PROGRESSION_LENGTH - 1)

    progression_list = generate_progression(first_number,
                                            common_difference,
                                            PROGRESSION_LENGTH)

    answer = progression_list.pop(hidden_element_index)
    progression_list.insert(hidden_element_index, '..')
    question = ' '.join(map(str, progression_list))

    return (str(question), str(answer))
