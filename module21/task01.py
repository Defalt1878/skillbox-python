print('Задача 1. Challenge 2')


def print_nums(_max: int):
    if _max > 1:
        print_nums(_max - 1)
    print(_max)


num = int(input('Введите num: '))
print_nums(num)
