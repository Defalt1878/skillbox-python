print('Задача 10. Симметричная последовательность')


def is_palindrome(_list: list):
    for i in range(0, len(_list) // 2):
        if _list[i] != _list[-(i + 1)]:
            return False
    return True


def get_missing_sequence(source: list):
    for i in range(len(source)):
        if is_palindrome(source[i:]):
            return list(reversed(source[:i]))


count = int(input('Кол-во чисел: '))
sequence = []

for _ in range(count):
    sequence.append(int(input('Число: ')))

missing = get_missing_sequence(sequence)

print('\nПоследовательность:', sequence)
print('Нужно приписать чисел:', len(missing))
print('Сами числа:', missing)
