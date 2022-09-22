print('Задача 3. Посчитай чужую зарплату...')

salary_sum = 0

for i in range(1, 13):
    salary_sum += int(input(f'Введите зарплату за месяц {i}:'))

print('Средняя зарплата за год равна', salary_sum / 12, 'рублей.')
