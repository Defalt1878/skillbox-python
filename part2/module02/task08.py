from collections import deque

print('Задача 7. Контейнеры')


def shift_elements(source: list, n: int):
    items = deque(source)
    items.rotate(n)
    return list(items)


elements = []

count = int(input('Количество элементов: '))
for e in range(count):
    elements.append(input('Введите элемент: '))

shift = int(input('Сдвиг: '))
print('Изначальный список:', elements)
print('Сдвинутый список:', shift_elements(elements, shift))
