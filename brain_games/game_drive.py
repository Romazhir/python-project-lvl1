# движок

# добавь импорты
import prompt


def play_game(rules_game, games_question, check_right_answer):
    print('Welcome to the Brain Games!')

    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(rules_game())

    ATTEMPTS_QUANTITY = 3
    attempts_counter = 1

    while attempts_counter <= ATTEMPTS_QUANTITY:
        question = games_question()
        print('Question: {}'.format(question))

        right_answer = check_right_answer(question)
        user_answer = input('Your answer: ')

        if user_answer == right_answer:
            print('Correct!')
            attempts_counter += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".
                  format(user_answer, right_answer))
            print("Let's try again, {}!".format(user_name))
            return

    print('Congratulations, {}!'.format(user_name))
