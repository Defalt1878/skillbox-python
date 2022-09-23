print('Задача 7. Опять?')


def minimum_number(x: float, y: float):
    return (x + y - abs(x - y)) / 2


x = float(input('Введите первое число: '))
y = float(input('Введите второе число: '))
print('Минимальное число: ', minimum_number(x, y))
