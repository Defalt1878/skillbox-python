print('Задача 2. И снова zip')

letters: list[str] = ['a', 'b', 'c', 'd', 'e']
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]

zipped = list(map(lambda x, y: (x, y), letters, numbers))

print(zipped)
