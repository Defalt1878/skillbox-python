print('Задача 10. Своя функция zip')


def my_zip(*iterables):
    iters = [iter(iterable) for iterable in iterables]
    try:
        while iters:
            result = []
            for it in iters:
                elem = next(it)
                result.append(elem)
            yield tuple(result)
    except StopIteration:
        return


s = 'abcd'
numbers_tuple = (10, 20, 30, 40)

print('Строка:', s)
print('Кортеж чисел:', numbers_tuple)

print('\nРезультат:')
for e in my_zip(s, numbers_tuple):
    print(e)
