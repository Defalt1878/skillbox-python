print('Задача 4. Крест')

side = int(input('Введите длину стороны квадрата: '))

for row in range(side):
    for col in range(side):
        if row == col or row == side - col - 1:
            print('^', end='')
        else:
            print(' ', end='')
    print()
