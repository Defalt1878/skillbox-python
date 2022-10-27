import random

print('Задача 3. Счастливое число')

remaining = 777
# noinspection PyBroadException
try:
    with open('out_file.txt', 'w') as out_file:
        while remaining > 0:
            number = int(input('Введите число: '))
            if random.randint(1, 13) == 13:
                raise Exception
            remaining -= number
            out_file.write(f'{str(number)}\n')
except Exception:
    print('Вас постигла неудача!')
else:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
