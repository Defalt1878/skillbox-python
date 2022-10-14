import re

print('Задача 5. Пароль')

password_pattern = re.compile(r'^(?=(.*\d){3,})(?=.*[A-Z]).{8,}$')

while True:
    password = input('Придумайте пароль: ')
    if password_pattern.match(password):
        break
    print('Пароль ненадёжный. Попробуйте ещё раз.')

print('Это надёжный пароль!')

# def password_strong(_password: str):    # Простая проверка без использования регулярных выражений.
#     return len(_password) >= 8 and \
#            sum(c.isupper() for c in _password) > 0 and \
#            sum(c.isdigit() for c in _password) >= 3
