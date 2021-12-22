#!/usr/bin/env python

from brain_games.game_drive import play_game
from brain_games.games.gcd_game import rules_gcd
from brain_games.games.gcd_game import get_gcd_question_string
from brain_games.games.gcd_game import get_gcd_right_answer


def main():
    play_game(rules_gcd, get_gcd_question_string, get_gcd_right_answer)


if __name__ == '__main__':
    main()
