# функции для brain-prime


# определяем правильный ответ
def get_prime_right_answer(question_number):
    divisor = 2
    while (divisor ** 2 <= question_number) and (question_number
                                                 % divisor != 0):
        divisor += 1
    if (divisor ** 2 > question_number) is True:
        return 'yes'
    else:
        return 'no'

# print(get_prime_right_answer(113))
