import os.path

print('Задача 5. Сохранение')


def write_file(file_path: str, data: str):
    if os.path.exists(file_path):
        if input('Вы действительно хотите перезаписать файл? ') == 'да':
            file = open(file_path, 'w')
            file.write(data)
            file.close()
            print('Файл успешно перезаписан!')
        else:
            print('Файл не изменён')
    else:
        file = open(file_path, 'w')
        file.write(data)
        file.close()
        print('Файл успешно сохранён!')
    print('\nСодержимое файла:')
    file = open(file_path, 'r')
    print(file.read())
    file.close()


text = input('Введите строку: ')

print('\nКуда хотите сохранить документ? Введите последовательность папок (через пробел):')
path = input().split()
path = os.path.join(*path)
if not os.path.exists(path):
    print('Ошибка. Путь не найден!')
    quit()

file_name = input('\nВведите имя файла: ')
full_path = os.path.join(path, file_name + '.txt')

write_file(full_path, text)
