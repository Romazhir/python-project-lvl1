#!/usr/bin/env python

from brain_games.even_game import get_user_name
from brain_games.even_game import get_question_number
from brain_games.even_game import get_right_answer
from brain_games.even_game import get_user_answer
from brain_games.even_game import get_game_result


def main():
    print('Welcome to the Brain Games!')

    user_name = get_user_name()

    print('Hello, {}!'.format(user_name))
    print('Answer "yes" if the number is even, otherwise answer "no".')

    def to_play_even_game():
        attempt = 1
        while attempt <= 3:
            question_number = get_question_number()
            print('Question: {}'.format(question_number))

            right_answer = get_right_answer(question_number)
            user_answer = get_user_answer()

            game_result = get_game_result(right_answer, user_answer)

            if game_result is True:
                print('Correct!')
                attempt += 1
            else:
                print("'{}' is wrong answer ;(. Correct answer was '{}'.".
                      format(user_answer, right_answer))
                print("Let's try again, {}!".format(user_name))
                return False
        return True

    if to_play_even_game() is True:
        print('Congratulations, {}!'.format(user_name))


if __name__ == '__main__':
    main()
