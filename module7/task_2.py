print('Задача 2. Должники')

result_sum = 0
for i in range(10):
    number = int(input('Введите число:'))
    if number % 2 == 0 and number > 0:
        result_sum += 1

print(result_sum, 'чисел являются четными и положительными')
