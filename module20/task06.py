print('Задача 6. По парам')


def split_to_pairs_1(source: list):
    result = []
    first_of_pair = 0
    for index, value in enumerate(source):
        if index % 2 == 0:
            first_of_pair = value
        else:
            result.append((first_of_pair, value))

    return result


def split_to_pairs_2(source: list):
    return list(zip(
        [even for index, even in enumerate(source) if index % 2 == 0],
        [odd for index, odd in enumerate(source) if index % 2 == 1]
    ))


original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert split_to_pairs_1(original) == split_to_pairs_2(original)

print('Оригинальный список: ', original)
print('Новый список: ', split_to_pairs_1(original))
