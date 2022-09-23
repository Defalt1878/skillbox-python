print('Задача 8. НОД')


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))

print(f'\nНОД {x} и {y} равен {gcd(x, y)}.')
