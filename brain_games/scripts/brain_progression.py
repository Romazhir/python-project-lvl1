#!/usr/bin/env python

from brain_games.game_drive import play_game
from brain_games.games.progression_game import rules_progression
from brain_games.games.progression_game import get_progression_question
from brain_games.games.progression_game import get_progression_right_answer


def main():
    play_game(rules_progression,
              get_progression_question,
              get_progression_right_answer)


if __name__ == '__main__':
    main()
