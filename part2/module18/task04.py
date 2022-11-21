import re

print('Задача 4. Телефонные номера')

phone_numbers = ['9999999999', '999999-999', '99999x9999']

print('Корректные номера:', [number for number in phone_numbers if re.match(r'^[89]\d{9}$', number)])
