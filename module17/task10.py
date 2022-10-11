print('Задача 10. Шифр Цезаря')

alphabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def cesar_encrypt_letter(letter: str, _shift: int):
    if letter in alphabet_upper:
        alphabet = alphabet_upper
    elif letter in alphabet_lower:
        alphabet = alphabet_lower
    else:
        return letter

    return alphabet[(alphabet.index(letter) + shift) % len(alphabet)]


def cesar_encrypt(_message: str, _shift: int):
    return ''.join([cesar_encrypt_letter(letter, shift) for letter in _message])


print('Шифруются только русские буквы.\n')

message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

print('\nЗашифрованное сообщение:', cesar_encrypt(message, shift))
