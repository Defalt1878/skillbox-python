print('Задача 2. Функция максимума')


def max_for_three(num_1, num_2, num_3):
    return max(max(num_1, num_2), max(num_2, num_3))


first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
third_number = float(input("Введите третье число: "))

print('Максимальное число из трех равно:', max_for_three(first_number, second_number, third_number))
