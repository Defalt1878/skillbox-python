import random

print('Задача 6. Сжатие списка')

count = int(input('Количество чисел в списке: '))

source = [random.randint(0, 2) for _ in range(count)]
zeros_in_end = [x for x in source if x != 0] + [0] * source.count(0)
compressed = [x for x in source if x != 0]

print('Список до сжатия:', source)
print('Список с нулями переставленными в конец:', zeros_in_end)
print('Список после сжатия:', compressed)
