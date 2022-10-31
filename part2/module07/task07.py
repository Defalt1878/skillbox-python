print('Задача 7. Функция сортировки')


def tpl_sort(*source):
    if len([val for val in source if not isinstance(val, int)]) != 0:
        return source
    return tuple(sorted(source))


assert tpl_sort(6, 3, -1, 8, 4, 10, -5) == (-5, -1, 3, 4, 6, 8, 10)
assert tpl_sort(6, 3, -1, 8, 4, 10, '-5') == (6, 3, -1, 8, 4, 10, '-5')
assert tpl_sort(6, 3, -1, 8, 4, 10, -5.5) == (6, 3, -1, 8, 4, 10, -5.5)
