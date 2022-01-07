import prompt


ROUND_NUMBERS = 3

def play_game(game):
    print('Welcome to the Brain Games!')

    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(game.RULE)

    for round in range(0, ROUND_NUMBERS):
        question_answer = tuple(game.generate_question_answer())
        question = question_answer[0]
        answer = question_answer[1]

        print('Question: {}'.format(question))
        user_answer = input('Your answer: ')

        if user_answer == answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".
                  format(user_answer, answer))
            print("Let's try again, {}!".format(user_name))
            return

    print('Congratulations, {}!'.format(user_name))
