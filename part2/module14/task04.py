import functools
from itertools import chain
from typing import Callable

print('Задача 4. Дебаг')


def parse_args_to_str(*args, **kwargs) -> str:
    args = (repr(arg) for arg in args)
    kwargs = (f'{name}={repr(value)}' for name, value in kwargs.items())
    return ', '.join(chain(args, kwargs))


def debug(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print(f'Вызывается {func.__name__}({parse_args_to_str(*args, **kwargs)})')
        result = func(*args, **kwargs)
        print(f'\'{func.__name__}\' вернула значение {repr(result)}')
        return result

    return wrapped_func


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


print(greeting("Том"), end='\n\n')
print(greeting("Миша", age=100), end='\n\n')
print(greeting(name="Катя", age=16), end='\n\n')
