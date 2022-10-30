print('Задача 1. Имена 2')

error_pattern = 'Ошибка: менее трёх символов в строке {}.'
symbols_count = 0

with open('people.txt', 'r', encoding='utf-8') as people_file, open('errors.log', 'a', encoding='utf-8') as log_file:
    for line_i, line in enumerate(people_file):
        try:
            length = len(line) - line.count('\n')
            symbols_count += length
            if length < 3:
                raise ValueError(error_pattern.format(line_i + 1))
        except ValueError:
            print(error_pattern.format(line_i + 1))
            log_file.write(error_pattern.format(line_i + 1) + '\n')
            # Максимально странное условие: кидаем ошибку и тут же ее глушим, чтобы продолжить выполнение.
            # Собственно, как и все задачи этого курса, добавлено просто чтобы было, без какого-либо смысла.
            # Но тут они превзошли себя, сложно представить куда уж хуже.

print(f'Общее количество символов: {symbols_count}.')
