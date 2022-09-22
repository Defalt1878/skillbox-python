print('Задача 4. Театр')

rows_amount = int(input('Введите кол-во рядов: '))
seats_amount = int(input('Введите кол-во сидений в ряде: '))
rows_distance = int(input('Введите кол-во метров между рядами: '))

print('\nСцена\n')

for i in range(rows_amount):
    print('=' * seats_amount, end=' ')
    print('*' * rows_distance, end=' ')
    print('=' * seats_amount)
