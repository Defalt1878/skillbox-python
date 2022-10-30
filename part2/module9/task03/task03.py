import re

print('Задача 3. Дзен Пайтона 2')


def get_letters(data: str):
    return [e for e in data if re.match('[a-zA-Z]', e)]


def get_words(data: str):
    return re.findall('[a-zA-Z\']+', data)


def get_rarest(letters_list: list[str]):
    letters_lower = [letter.lower() for letter in letters_list]

    letters_count = [(letters_lower.count(e), e) for e in set(letters_lower)]
    letters_count.sort()

    return letters_count[0][1]


zen_file = open('zen.txt', 'r')
zen = zen_file.read()
zen_file.close()

letters = get_letters(zen)
print('Количество букв в файле:', len(letters))
print('Количество слов в файле:', len(get_words(zen)))
print('Количество строк в файле:', len(zen.split('\n')))
print('Наиболее редкая буква:', get_rarest(letters))
