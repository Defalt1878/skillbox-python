print('Задача 8. Сумма ряда')

n = int(input('Введите число: '))

result = 0

for number in range(n + 1):
    result += ((-1) ** number) * 1 / (2 ** number)

print(result)
