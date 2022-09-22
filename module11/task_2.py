import math

print('Задача 2. Грубая математика')

count = int(input('Введите кол-во чисел: '))

for i in range(count):
    number = float(input('Введите число: '))

    if number > 0:
        number = math.ceil(number)
        print(f'x = {number} log(x) = {math.log(number)}')
    elif number < 0:
        number = math.floor(number)
        print(f'x = {number} exp(x) = {math.exp(number)}')
