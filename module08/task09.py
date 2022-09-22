print('Задача 9. Выражение')

x = int(input('Введите число: '))

numerator = 1
denominator = 1

for r in range(1, 7):
    coeff = 2 ** r
    numerator *= (x - (coeff - 1))
    denominator *= (x - coeff)

if denominator == 0:
    print('Невозможно разделить на ноль.')
else:
    print('Результат: ', numerator / denominator)
