# функции для brain-gcd

# определяем наибольший делитель
def get_gcd_right_answer(question_number_1, question_number_2):
    question_numbers_list = [question_number_1, question_number_2]
    question_numbers_list.sort()

    num1 = question_numbers_list[0]  # меньшее число
    num2 = question_numbers_list[1]  # большее число

    if num2 % num1 == 0:
        return num1

    divisor = num1 // 2
    while divisor > 0:
        if num1 % divisor == 0:
            if num2 % divisor == 0:
                return divisor
        divisor -= 1

# print(get_gcd_right_answer(145, 15))
