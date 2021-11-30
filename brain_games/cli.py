import prompt


def welcome_user():
    name_user = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name_user))
