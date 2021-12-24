#!/usr/bin/env python

from brain_games.game_drive import play_game
from brain_games.games.prime_game import rules_prime
from brain_games.games.prime_game import get_prime_question_number
from brain_games.games.prime_game import get_prime_right_answer


def main():
    play_game(rules_prime,
              get_prime_question_number,
              get_prime_right_answer)


if __name__ == '__main__':
    main()
