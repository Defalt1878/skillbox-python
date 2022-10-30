print('Задача 3. Апгрейд калькулятора')


def get_operation():
    print_menu()
    operation = input('Что сделать: ').lower()

    if operation in {'sum', 'max', 'min', 'quit'}:
        return operation

    print('Неизвестная операция, попробуйте еще раз.')
    get_operation()


def print_menu():
    print('\nДоступные операции:')
    print('sum - Вывести сумму его цифр')
    print('max - Вывести максимальную цифру')
    print('min - Вывести минимальную цифру')
    print('quit - Выход\n')


def print_digits_sum(num: int):
    print('Сумма чисел:', sum(get_digits(num)))


def print_max_digit(num: int):
    print('Максимальное число:', max(get_digits(num)))


def print_min_digit(num: int):
    print('Минимальное число:', min(get_digits(num)))


def get_digits(num: int):
    return map(int, str(num))


while True:
    number = int(input('Введите число: '))

    match get_operation():
        case 'sum':
            print_digits_sum(number)
        case 'max':
            print_max_digit(number)
        case 'min':
            print_min_digit(number)
        case 'quit':
            quit()
    print()
