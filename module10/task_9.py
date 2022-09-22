print('Задача 9. Пирамидка 2')

size = int(input('Введите количество уровней пирамиды: '))

current_number = 1
for level in range(1, size + 1):
    print('\t' * (size - level), end='')
    for i in range(level):
        print(current_number, end='\t\t')
        current_number += 2
    print()
