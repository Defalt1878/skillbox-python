print('Задача 4. Среднее на отрезке')
a = int(input('Введите левую границу отрезка: '))
b = int(input('Введите правую границу отрезка: '))
c = int(input('Введите число для проверки кратности: '))

three_multiple_sum = 0
three_multiple_count = 0
for n in range(a + c - a % c, b + 1, c):
    three_multiple_sum += n
    three_multiple_count += 1

print(f'Среднее арифметическое всех чисел кратных {c}: {three_multiple_sum / three_multiple_count}')
