from math import sqrt

print('Задача 9. Уравнение')

a = float(input('Введите коэффициент a: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))

discriminant = b * b - 4 * a * c

if discriminant == 0:
    print(- b / (2 * a))
elif discriminant > 0:
    print((- b - sqrt(discriminant)) / (2 * a), end='\t')
    print((- b + sqrt(discriminant)) / (2 * a))
else:
    print('Нет действительных корней.')
