print('Задача 4. Урок информатики 3')

number = input('Введите число в экспоненциальной форме: ').lower()
tokens = number.split('e')

print('Мантисса:', float(tokens[0]))
print('Порядок числа:', int(tokens[1]))
