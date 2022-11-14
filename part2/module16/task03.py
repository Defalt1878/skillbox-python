import functools
import re
import time
from datetime import datetime
from typing import Callable, Optional

print('Задача 3. Логирование в формате')


def parse_date_format(dateformat: str) -> str:
    return re.sub(r'(-?[dmyHIMSj]|[aAwbBYpfzZUWcxX%])', r'%\1', dateformat)


def log_method(_func: Optional[Callable] = None, *, dateformat: str = "b d Y - H:M:S") -> Callable:
    dateformat = parse_date_format(dateformat)

    def method_logger_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Callable:
            print(f'Запускается \'{func.__qualname__}\'. Дата и время запуска: {datetime.now().strftime(dateformat)}')
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start
            print(f'Завершение \'{func.__qualname__}\', время работы = {duration:.3f}s')
            return result

        return wrapped_func

    if _func is None:
        return method_logger_decorator
    else:
        return method_logger_decorator(_func)


def log_methods(dateformat: str) -> Callable:
    def methods_logger_decorator(cls):
        for method_name in dir(cls):
            if not method_name.startswith('__'):
                method = getattr(cls, method_name)
                decorated = log_method(method, dateformat=dateformat)
                setattr(cls, method_name, decorated)
        return cls

    return methods_logger_decorator


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
