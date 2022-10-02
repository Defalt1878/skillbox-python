print('Задача 3. Клетки')


def get_bad_cells(source: list):
    result = []
    for i in range(len(source)):
        if source[i] < i:
            result.append(source[i])
    return result


cells = []

count = int(input('Количество клеток: '))
for cell in range(1, count + 1):
    cells.append(int(input(f'Эффективность {cell} клетки: ')))

print('Неподходящие значения: ', ' '.join(map(str, get_bad_cells(cells))))
