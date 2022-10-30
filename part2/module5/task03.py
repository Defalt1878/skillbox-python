print('Задача 3. Файлы')

SPECIAL_SYMBOLS = {'@', '№', '$', '%', '^', '&', '*', '(', ')'}

file_name = input('Название файла: ')

if file_name[0] in SPECIAL_SYMBOLS:
    print('Ошибка: название начинается на один из специальных символов.')
elif not (file_name.endswith('.txt') or file_name.endswith('.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')
