print('Задача 2. Свой zip 2')


def my_zip(*iterables):
    iterators = [iter(iterable) for iterable in iterables]
    return (
        tuple([next(iterator) for iterator in iterators])
        for _
        in range(min([len(iterable) for iterable in iterables]))
    )


print(my_zip([10, 20, 30, 40], 'abc'))

assert list(my_zip([10, 20, 30, 40], 'abc')) == [(10, 'a'), (20, 'b'), (30, 'c')]
assert list(my_zip([10, 20], 'abc', {5.5})) == [(10, 'a', 5.5)]
