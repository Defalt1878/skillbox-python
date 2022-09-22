print('Задача 7. Великий и могучий')

text = input('Введите текст: ')
result = max(map(lambda s: len(s), text.split(' ')))
print('Самое длинное слово, букв:', result)
