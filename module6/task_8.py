print('Задача 8. Вклады')

deposit = int(input('Введите начальную сумму вклада: '))
interest_rate = int(input('Введите ежегодную процентную ставку: '))
result_money = int(input('Введите сумму которую желаете накопить: '))

years = 0
while deposit < result_money:
    deposit *= 1 + interest_rate / 100
    deposit //= 1
    years += 1

print(f'Для накопления понадобится {years} лет')
