import os
from collections.abc import Iterator

print('Задача 5. Количество строк')


def get_py_file_lines_count(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for line in file if line.lstrip() and not line.lstrip().startswith('#'))


def get_py_files_lines_count_in_dir(dir_path: str) -> Iterator[str, int]:
    for py_file in (file for file in os.listdir(dir_path) if file.endswith('.py')):
        abs_path = os.path.abspath(os.path.join(dir_path, py_file))
        yield abs_path, get_py_file_lines_count(abs_path)


for file_path, count in get_py_files_lines_count_in_dir('..\\module13'):
    print(f'{file_path}: {count}')
