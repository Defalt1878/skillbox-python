print('Задача 4. Регистрация')


def check_correct_data(data: str):
    tokens = data.split()
    if len(tokens) != 3:
        raise IndexError('НЕ присутствуют все три поля')
    if not tokens[0].isalpha():
        raise NameError('Поле имени содержит НЕ только буквы')
    if not ('@' in tokens[1] and '.' in tokens[1]):
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку)')
    if not (tokens[2].isnumeric() and 10 <= int(tokens[2]) <= 99):
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')


with open('registration.txt', 'r', encoding='utf-8') as source, \
        open('registrations_good.log', 'w', encoding='utf-8') as good_log, \
        open('registrations_bad.log', 'w', encoding='utf-8') as bad_log:
    for line in source:
        line = line.replace('\n', '')
        try:
            check_correct_data(line)
        except Exception as e:
            bad_log.write(f'{line}    {str(e)}\n')
        else:
            good_log.write(f'{line}\n')
