import functools
from typing import Callable

print('Задача 2. Функция обратного вызова')

app = dict()


def callback(_route: str) -> Callable:
    def callback_decorator(func: Callable) -> Callable:
        app[_route] = func

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapped_func

    return callback_decorator


@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
