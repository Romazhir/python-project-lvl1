# функции для brain-even

# Определяем правильный ответ, исходя из числа для игры
def get_even_right_answer(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'

# test_number = randint(1,999)
# print(test_number)
# print(get_right_answer(test_number))
