print('Задача 6. Сумма факториалов')

n = int(input('Введите число N: '))
result_sum = temp_number = 1

for i in range(2, n + 1):
    temp_number *= i
    result_sum += temp_number

print('Сумма факториалов равна:', result_sum)
