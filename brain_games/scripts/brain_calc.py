#!/usr/bin/env python

from brain_games.game_drive import play_game
from brain_games.games.calc_game import rules_calc
from brain_games.games.calc_game import get_calc_question_expression
from brain_games.games.calc_game import get_calc_right_answer


def main():
    play_game(rules_calc, get_calc_question_expression, get_calc_right_answer)


if __name__ == '__main__':
    main()
