print('Задача 9. Ханойские башни')

output_pattern = 'Переложить диск {} со стержня номер {} на стержень номер {}'


def move(disk, start, end):
    auxiliary = 6 - start - end

    if disk == 1:
        print(output_pattern.format(disk, start, end))
        return

    move(disk - 1, start, auxiliary)
    print(output_pattern.format(disk, start, end))
    move(disk - 1, auxiliary, end)


count = int(input('Введите количество дисков: '))
move(count, 1, 3)
