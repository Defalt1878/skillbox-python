print('Задача 8. Список списков 2')


def deep_flat_map(iterable):
    if isinstance(iterable, str):
        yield iterable
        return
    try:
        iterator = iter(iterable)
        while True:
            nested = next(iterator, None)
            if nested is None:
                break
            for e in deep_flat_map(nested):
                yield e
    except TypeError:
        yield iterable


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
assert list(deep_flat_map(nice_list)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
