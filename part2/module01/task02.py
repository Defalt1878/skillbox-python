print('Задача 2. Сессия')

print('Введите первую точку')
x1 = float(input('X: '))
y1 = float(input('Y: '))

print('\nВведите вторую точку')
x2 = float(input('X: '))
y2 = float(input('Y: '))

dx = x1 - x2
dy = y1 - y2
if dx == dy == 0:
    print('Невозможно построить уравнение прямой.')
    quit()

print('Уравнение прямой, проходящей через эти точки:')

if dx == 0:
    print(f'x = {x1}')
else:
    k = dy / dx
    b = y1 - k * x1
    print(f'y = {k} * x + {b}')
