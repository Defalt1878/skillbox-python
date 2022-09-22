print('Задача 7. Наибольшая сумма цифр')

count = int(input('Введите количество чисел: '))
max_sum_number = max_sum = 0

for i in range(count):
    number = int(input('Введите натуральное число: '))
    digits_sum = sum(map(lambda d: int(d), str(number)))

    if digits_sum > max_sum:
        max_sum_number = number
        max_sum = digits_sum

print(f'У числа {max_sum_number} наибольшая сумма чисел, равная {max_sum}')
