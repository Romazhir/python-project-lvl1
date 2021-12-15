#!/usr/bin/env python

from brain_games.games.all_games import get_user_name
from brain_games.games.all_games import get_question_number
from brain_games.games.all_games import get_user_answer
from brain_games.games.all_games import get_game_result
from brain_games.games.progression_game import get_game_list
from brain_games.games.progression_game import get_hidden_element
from brain_games.games.progression_game import get_game_list_for_player


def main():  # noqa: C901
    print('Welcome to the Brain Games!')

    user_name = get_user_name()

    print('Hello, {}!'.format(user_name))
    print('What number is missing in the progression?')

    def to_play_progression_game():
        attempt = 1
        while attempt <= 3:
            start_number = get_question_number()
            progression_step = get_question_number()
            quantity_elements = 10

            game_list = get_game_list(start_number,
                                      quantity_elements, progression_step)
            hidden_element = get_hidden_element()
            game_list_for_player = (get_game_list_for_player
                                    (hidden_element, game_list))

            print('Question:', *game_list_for_player, sep=' ')

            right_answer = game_list[hidden_element]
            user_answer = get_user_answer()

            def to_check_answer_type(string):
                try:
                    int(string)
                    return True
                except ValueError:
                    return False

            if to_check_answer_type(user_answer) is True:
                game_result = get_game_result(right_answer, int(user_answer))
            else:
                game_result = False

            if game_result is True:
                print('Correct!')
                attempt += 1
            else:
                print("'{}' is wrong answer ;(. Correct answer was '{}'.".
                      format(user_answer, right_answer))
                print("Let's try again, {}!".format(user_name))
                return False
        return True
    if to_play_progression_game() is True:
        print('Congratulations, {}!'.format(user_name))


if __name__ == '__main__':
    main()
