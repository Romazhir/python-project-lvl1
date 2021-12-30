import prompt


def play_game(game):
    print('Welcome to the Brain Games!')

    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(game.RULES)

    ROUND_NUMBERS = 3
    round_count = 1

    while round_count <= ROUND_NUMBERS:
        print('Question: {}'.format(game.question))
        user_answer = input('Your answer: ')

        if user_answer == game.right_answer:
            print('Correct!')
            round_count += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".
                  format(user_answer, game.right_answer))
            print("Let's try again, {}!".format(user_name))
            return

    print('Congratulations, {}!'.format(user_name))
