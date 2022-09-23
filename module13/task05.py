print('Задача 5. Недоделка 2')


def swap_digits(number: int):
    number = list(str(number))
    (number[0], number[len(number) - 1]) = (number[len(number) - 1], number[0])
    return int(''.join(number))


def get_modified_number(min_digits_count: int):
    num = int(input(f'Введите число (не менее {min_digits_count} цифр): '))
    if len(str(num)) < min_digits_count:
        print(f'Ошибка ввода! Меньше {min_digits_count} цифр!')
        quit()
    num = swap_digits(num)
    print('Изменённое число:', num)
    return num


first = get_modified_number(3)
second = get_modified_number(4)

print('Сумма чисел:', first + second)
