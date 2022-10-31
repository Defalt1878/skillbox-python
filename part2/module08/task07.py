print('Задача 7. Продвинутая функция sum')


def deep_flat_map(iterable):
    iters_stack = [iter(iterable)]
    while iters_stack:
        iterator = iters_stack.pop()
        while True:
            n = next(iterator, None)
            if n is None:
                break
            if isinstance(n, str) and len(n) == 1:
                yield n
                continue
            try:
                iters_stack.append(iter(n))
            except TypeError:
                yield n


def sum_improved(*args):
    result = 0
    for e in deep_flat_map(args):
        result += e
    return result


actual = sum_improved(1, 2, 3, 4, 5)
assert actual == 15

actual = sum_improved([1, 2, 3, 4, 5])
assert actual == 15

actual = sum_improved([[1, 2, [3]], [1], 3])
assert actual == 10

actual = sum_improved(5)
assert actual == 5
