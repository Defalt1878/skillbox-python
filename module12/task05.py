print('Задача 5. Текстовый редактор')


def count_letters(string: str, digit: int, symbol: str):
    digits_count = string.count(str(digit))
    symbols_count = string.count(symbol)
    print(f'\nКоличество цифр {digit}: {digits_count}')
    print(f'Количество букв {symbol}: {symbols_count}')


text = input('Введите текст: ')
number = int(input('Какую цифру ищем? '))
letter = input('Какую букву ищем? ')
count_letters(text, number, letter)
