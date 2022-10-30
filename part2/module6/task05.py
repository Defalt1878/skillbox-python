print('Задача 5. Гистограмма частоты 2')


def get_letters_count(src: str):
    result = dict()
    for symbol in src:
        result[symbol] = result.get(symbol, 0) + 1

    return result


def invert_dict(src: dict):
    inverted = {}
    for key, value in src.items():
        inverted[value] = inverted.get(value, []) + [key]

    return inverted


def to_string(_dict: dict):
    return '\n'.join(f'{key} : {value}' for key, value in _dict.items())


text = input('Введите текст: ')

frequencies = get_letters_count(text)
print('\nОригинальный словарь частот:')
print(to_string(frequencies))

inverted_frequencies = invert_dict(frequencies)
print('\nИнвертированный словарь частот:')
print(to_string(inverted_frequencies))
