print('Задача 5. Функция 2')

start = int(input('Введите начало отрезка: '))
end = int(input('Введите конец отрезка: '))
step = int(input('Ведите шаг: '))

for x in range(end, start - 1, step):
    y = x ** 3 + 2 * x * x - 4 * x + 1
    print('В точке', x, 'функция равна', y)
