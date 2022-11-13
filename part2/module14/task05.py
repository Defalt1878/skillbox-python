import functools
from typing import Callable

print('Задача 5. Счётчик')


# noinspection PyDefaultArgument
def invoke_counter(func: Callable, calls_count=dict()) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        calls_count[func] = calls_count.get(func, 0) + 1
        print(f'Функция {func.__name__} вызвана {calls_count[func]} раз.')
        return func(*args, **kwargs)

    return wrapped_func


@invoke_counter
def test_1():
    pass


@invoke_counter
def test_2():
    pass


for i in range(51):
    test_1()
    if i % 5 == 0:
        test_2()
