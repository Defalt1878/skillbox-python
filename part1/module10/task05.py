print('Задача 5. Простые числа')

count = int(input('Введите кол-во чисел: '))
counter = 0

for i in range(count):
    number = int(input('Введите число: '))

    if number == 2 or number == 3:
        counter += 1
        continue
    if number % 2 == 0 or number < 2:
        continue
    for j in range(3, int(number ** 0.5) + 1, 2):
        if number % j == 0:
            continue

    counter += 1

print('\nКоличество простых чисел в последовательности:', counter)
