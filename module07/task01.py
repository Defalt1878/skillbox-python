print('Задача 1. Тайны археологии')

for number in 114, 12, 14, 10605, 4907, 450:
    if number % 2 == 0 and number % 3 != 0:
        print('Число', number, 'подходит')
    else:
        print('Число', number, 'не подходит')
