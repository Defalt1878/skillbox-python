print('Задача 10. Снова палиндром   ')


def get_letters_count(_str: str):
    result = dict()
    for symbol in _str:
        result[symbol] = result.get(symbol, 0) + 1

    return result


def can_be_palindrome(_str: str):
    odd_counts = [count for count in get_letters_count(_str).values() if count % 2 == 1]
    return len(odd_counts) < 2


s = input('Введите строку: ')
print('Можно сделать палиндромом' if can_be_palindrome(s) else 'Нельзя сделать палиндромом')
