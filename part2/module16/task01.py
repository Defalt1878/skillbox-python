import functools
from typing import Callable, Any

print('Задача 1. Права доступа')

user_permissions = ['admin']


def check_permission(required_permission: str) -> Callable:
    def permissions_checker_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            if required_permission not in user_permissions:
                raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
            return func(*args, **kwargs)

        return wrapped_func

    return permissions_checker_decorator


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
