print('Задача 6. Монетка')

AREA = 1


def check_coordinate(x, y):
    if abs(x) > AREA or abs(y) > AREA:
        return 'Монетки в области нет.'
    else:
        return 'Монетка где-то рядом.'


print(check_coordinate(int(input('Введите координату X: ')), int(input('Введите координату Y: '))))
