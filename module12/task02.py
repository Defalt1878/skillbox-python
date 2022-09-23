print('Задача 2. Функция в функции')


def test():
    number = int(input('Введите число: '))
    if number > 0:
        positive()
    elif number < 0:
        negative()


def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


test()
