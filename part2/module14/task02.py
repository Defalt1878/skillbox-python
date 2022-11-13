import functools
import time
from typing import Callable

print('Задача 2. Замедление кода')


def sleep_decorator_builder(time_to_sleep_in_seconds: float):
    def sleep(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            time.sleep(time_to_sleep_in_seconds)
            return func(*args, **kwargs)

        return wrapped_func

    return sleep


@sleep_decorator_builder(1)
def test():
    print('<Тут что-то происходит...>')


test()
