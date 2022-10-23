import os.path

print('Задача 4. Файлы и папки')


def walk_file_tree(start_path: str):
    size = 0
    subfolders_count = -1
    files_count = 0
    paths_stack = [start_path]

    while paths_stack:
        current_path = paths_stack.pop()
        if os.path.isfile(current_path):
            files_count += 1
            size += os.path.getsize(current_path)
        else:
            subfolders_count += 1
            for subfolder in os.listdir(current_path):
                paths_stack.append(os.path.join(current_path, subfolder))
    return size, subfolders_count, files_count


path = input('Введите путь каталога:\n')

result = walk_file_tree(path)

print('Размер каталога (в Кб): ', result[0] / 1024)
print('Количество подкаталогов: ', result[1])
print('Количество файлов: ', result[2])
