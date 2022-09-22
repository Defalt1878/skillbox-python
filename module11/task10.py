print('Задача 10. За что?')

x = float(input('Введите первое число: '))
y = float(input('Введите второе число: '))

maximum = (x + y + abs(x - y)) / 2

print('Наибольшее число:', maximum)
