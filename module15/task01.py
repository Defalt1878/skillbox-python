print('Задача 1. Генерация списка')


def get_odd_list(n: int):
    return list(range(1, n + 1, 2))


number = int(input('Введите число: '))
print('Список из нечётных чисел от одного до N:', get_odd_list(number))
