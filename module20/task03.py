print('Задача 3. Функция')


def slicer(source: tuple, borders_value: int):
    value_count = source.count(borders_value)
    if value_count == 0:
        return ()
    start = source.index(borders_value)
    if value_count == 1:
        return source[start:]
    else:
        return source[start:source.index(borders_value, start + 1) + 1]


assert slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2) == (2, 3, 4, 5, 6, 7, 8, 2)
assert slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 7) == (7, 8, 2, 2, 9, 10)
assert slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 12) == ()
