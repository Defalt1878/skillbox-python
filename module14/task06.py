print('Задача 6. Монетка 2')


def check_coordinate(x, y, r):
    dist = (x * x + y * y) ** 0.5
    return dist <= r


print('Введите координаты монетки:')
m_x = float(input('X: '))
m_y = float(input('Y: '))
radius = float(input('Введите радиус: '))

if check_coordinate(m_x, m_y, radius):
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')
