print('Задача 5. Ускоряем работу функции')


# noinspection PyDefaultArgument
def fact(value: int, calculated=[1, 1]):
    if value < 0:
        raise ValueError('Value cannot be less than zero.')
    for i in range(len(calculated), value + 1):
        calculated.append(calculated[i - 1] * i)
    return calculated[value]


def calculating_math_func(data: int):
    return (fact(data) / (data ** 3)) ** 10


print(calculating_math_func(10))
print(calculating_math_func(5))
print(calculating_math_func(2))
