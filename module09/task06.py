from re import split

print('Задача 6. Спецшифр')

string = input('Введите строку: ')
result = max(map(lambda s: len(s), split('[^s]+', string)))
print('Самая длинная последовательность:', result)
