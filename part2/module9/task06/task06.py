import string

print('Задача 6. Паранойя')

lower = string.ascii_lowercase
upper = string.ascii_uppercase


def clear_file(file: str):
    file = open(file, 'w')
    file.close()


def print_file(file: str):
    data = open(file, 'r')
    print(data.read())
    data.close()


def cesar_encrypt(data: str, shift: int):
    result = []
    for letter in data:
        if letter in lower:
            result.append(lower[(lower.index(letter) + shift) % len(lower)])
        elif letter in upper:
            result.append(upper[(upper.index(letter) + shift) % len(upper)])
        else:
            result.append(letter)

    return ''.join(result)


def cypher_file(source_file_path: str, result_file_path: str):
    source = open(source_file_path, 'r')
    clear_file(result_file_path)
    result = open(result_file_path, 'a')
    for i, line in enumerate(source):
        result.write(cesar_encrypt(line, i + 1))
    source.close()
    result.close()


cypher_file('text.txt', 'cipher_text.txt')

print('Содержимое файла text.txt:')
print_file('text.txt')

print('Содержимое файла cipher_text.txt:')
print_file('cipher_text.txt')
