import functools
from typing import Callable

print('Задача 4. Весь мир — декоратор...')


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorator_builder(*args, **kwargs) -> Callable:
        def wrapped_decorator(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)

        return wrapped_decorator

    return decorator_builder


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    """Декорированный декоратор"""

    @functools.wraps(func)
    def wrapped_func(*func_args, **func_kwargs) -> Callable:
        print("Переданные арги и кварги в декоратор:", dec_args, dec_kwargs)
        return func(*func_args, **func_kwargs)

    return wrapped_func


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    """Декорированная функция"""

    print("Привет", text, num)


decorated_function("Юзер", 101)
