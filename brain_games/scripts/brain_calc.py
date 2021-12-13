#!/usr/bin/env python

from brain_games.games.all_games import get_user_name
from brain_games.games.all_games import get_question_number
from brain_games.games.all_games import get_user_answer
from brain_games.games.all_games import get_game_result
from brain_games.games.calc_game import get_calc_operator
from brain_games.games.calc_game import get_calc_operator_symbol
from brain_games.games.calc_game import get_calc_right_answer


def main():  # noqa: C901
    print('Welcome to the Brain Games!')

    user_name = get_user_name()

    print('Hello, {}!'.format(user_name))
    print('What is the result of the expression?')

    def to_play_calc_game():
        attempt = 1
        while attempt <= 3:
            question_number_1 = get_question_number()
            question_number_2 = get_question_number()
            calc_operator = get_calc_operator()
            calc_operator_symbol = get_calc_operator_symbol(calc_operator)

            print('Question: {} {} {}'.format(question_number_1,
                                              calc_operator_symbol,
                                              question_number_2))

            right_answer = get_calc_right_answer(question_number_1,
                                                 question_number_2,
                                                 calc_operator)
            user_answer = get_user_answer()

            # не получалось импортировать эту функцию из модуля
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

    if to_play_calc_game() is True:
        print('Congratulations, {}!'.format(user_name))


if __name__ == '__main__':
    main()
