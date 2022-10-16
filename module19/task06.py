import re

print('Задача 6. Словарь синонимов')

synonyms = dict()

count = int(input('Введите количество пар слов: '))

for pair_i in range(1, count + 1):
    pair = re.split('[^а-яА-Яa-zA-Z]+', input(f'{pair_i}-я пара: '))
    if len(pair) != 2:
        print('Ошибка ввода!')
        continue

    synonyms[pair[0].lower()] = pair[1]
    synonyms[pair[1].lower()] = pair[0]

while True:
    word = input('\nВведите слово: ').lower()
    if word not in synonyms:
        print('Такого слова в словаре нет.')
    else:
        print('Синоним:', synonyms[word])
        break
