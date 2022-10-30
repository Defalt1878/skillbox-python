print('Задача 1. Гласные буквы')

vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
text = input('Введите текст: ')

vowels_in_text = [letter for letter in text if letter in vowels]

print('Список гласных букв:', vowels_in_text)
print('Длина списка:', len(vowels_in_text))
