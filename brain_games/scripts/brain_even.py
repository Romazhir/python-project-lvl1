#!/usr/bin/env python

from brain_games.game_drive import play_game
from brain_games.games.even_game import rules_even
from brain_games.games.even_game import get_question_number
from brain_games.games.even_game import get_even_right_answer


def main():
    play_game(rules_even, get_question_number, get_even_right_answer)


if __name__ == '__main__':
    main()
