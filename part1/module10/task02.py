print('Задача 2. Лестница')

rows_count = int(input('Введите число: '))

for row in range(1, rows_count + 1):
    for i in range(row):
        print(row, end=' ')
    print()
