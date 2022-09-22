print('Задача 10. Яма ')

n = int(input('Введите размер ямы: '))
print()

for row in range(1, n + 1):
    for i in range(n, n - row, -1):
        print(i, end='')
    print('.' * (2 * (n - row)), end='')
    for i in range(n - row + 1, n + 1):
        print(i, end='')
    print()
