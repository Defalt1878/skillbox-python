print('Задача 7. Опять?')


def minimum_number(x: float, y: float):
    return (x + y - abs(x - y)) / 2


print('Минимальное число: ', minimum_number(
    float(input('Введите первое число: ')),
    float(input('Введите второе число: '))
))
