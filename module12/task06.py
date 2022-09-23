print('Задача 6. Монетка')

AREA = 1


def check_coordinate(x, y):
    if abs(x) > AREA or abs(y) > AREA:
        print('Монетки в области нет.')
    else:
        print('Монетка где-то рядом.')


x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))
check_coordinate(x, y)
