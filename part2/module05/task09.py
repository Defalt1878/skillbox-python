import re

print('Задача 9. Сообщение')


def split_to_groups(source: str):
    return re.findall('[а-яА-Я]+|[^а-яА-Я]+', source)


def reverse_words(source: list[str]):
    return ''.join([e[::-1] if e.isalpha() else e for e in source])


message = input('Сообщение: ')
print('Новое сообщение:', reverse_words(split_to_groups(message)))
