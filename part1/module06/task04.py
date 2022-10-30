print('Задача 4. Календари')

month = 0
while True:
    days = int(input('Введите количество дней в месяце: '))
    if days == 0:
        break
    if days % 2 == 0:
        month += 1

print('Месяцев с четным количеством дней было:', month)
