print('Задача 3. Ряд Фибоначчи')


def get_fibonacci_number(pos: int):
    if pos < 1:
        raise ValueError('Pos cannot be less than one.')
    if pos < 3:
        return 1

    return get_fibonacci_number(pos - 2) + get_fibonacci_number(pos - 1)


def get_fibonacci_number_fast(pos: int):
    if pos < 1:
        raise ValueError('Pos cannot be less than one.')
    previous = [1, 1]
    for cur_pos in range(3, pos + 1):
        previous[cur_pos % 2] = sum(previous)

    return previous[pos % 2]


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число:', get_fibonacci_number_fast(num_pos))
