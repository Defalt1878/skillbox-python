print('Задача 3. Слишком большие числа')

number = int(input('Введите число: '))
count = 0
while number > 0:
    number //= 10
    count += 1

print(f'В числе {max(1, count)} цифр(а/ы).')
