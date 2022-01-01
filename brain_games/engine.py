import prompt


def play_game(game):
    print('Welcome to the Brain Games!')

    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(game.RULES)

    ROUND_NUMBERS = 3
    round_count = 1

    while round_count <= ROUND_NUMBERS:
        games_data = list(game.get_games_data())

        print('Question: {}'.format(games_data[0]))
        user_answer = input('Your answer: ')

        if user_answer == games_data[1]:
            print('Correct!')
            round_count += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".
                  format(user_answer, games_data[1]))
            print("Let's try again, {}!".format(user_name))
            return

    print('Congratulations, {}!'.format(user_name))
