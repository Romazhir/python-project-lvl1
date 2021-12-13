#!/usr/bin/env python

from brain_games.games.all_games import get_user_name
from brain_games.games.all_games import get_question_number
from brain_games.games.all_games import get_user_answer
from brain_games.games.all_games import get_game_result
from brain_games.games.gcd_game import get_gcd_right_answer


def main():  # noqa: C901
    print('Welcome to the Brain Games!')

    user_name = get_user_name()

    print('Hello, {}!'.format(user_name))
    print('Find the greatest common divisor of given numbers.')

    def to_play_gcd_game():
        attempt = 1
        while attempt <= 3:
            question_number_1 = get_question_number()
            question_number_2 = get_question_number()

            print('Question: {} {}'.format(question_number_1,
                                           question_number_2))

            right_answer = get_gcd_right_answer(question_number_1,
                                                question_number_2)
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
    if to_play_gcd_game() is True:
        print('Congratulations, {}!'.format(user_name))


if __name__ == '__main__':
    main()
