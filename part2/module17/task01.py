from functools import reduce

print('Задача 1. Новые списки')

floats: list[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: list[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: list[int] = [22, 33, 10, 6894, 11, 2, 1]

floats = list(map(lambda e: round(e ** 3, 3), floats))
names = list(filter(lambda s: len(s) >= 5, names))
numbers_product = reduce(lambda x, y: x * y, numbers)

print(floats)
print(names)
print(numbers_product)
