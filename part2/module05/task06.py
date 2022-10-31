import re

print('Задача 6. Сжатие')


def compress(source: str):
    repeats = [x.group() for x in re.finditer(r'(.)\1+|.', source)]
    print(repeats)
    return ''.join([f'{e[0]}{len(e)}' for e in repeats])


s = input('Введите строку: ')
print('Закодированная строка:', compress(s))
