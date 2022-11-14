import functools

print('Задача 5. Синглтон')


def singleton(cls):
    @functools.wraps(cls)
    def wrapped_cls(*args, **kwargs):
        if cls.__instance is None:
            cls.__instance = cls(*args, **kwargs)
        return cls.__instance

    cls.__instance = None
    return wrapped_cls


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
