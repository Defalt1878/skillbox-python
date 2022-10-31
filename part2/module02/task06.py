print('Задача 6. Анализ слова')


def unique_letters_count(source):
    letters_count = dict()
    for letter in source:
        if letter not in letters_count:
            letters_count[letter] = 0
        letters_count[letter] += 1
    return len(list(filter(lambda elem: elem[1] == 1, letters_count.items())))


word = input('Введите слово: ')
print('Количество уникальных букв:', unique_letters_count(word))
