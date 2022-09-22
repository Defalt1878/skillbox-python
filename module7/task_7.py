print('Задача 7. Отрезок')

a = int(input('Введите левую границу отрезка: '))
b = int(input('Введите правую границу отрезка: '))

three_multiple_sum = 0
three_multiple_count = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        three_multiple_sum += i
        three_multiple_count += 1

print('Среднее арифметическое чисел кратных трём:', three_multiple_sum / three_multiple_count)
