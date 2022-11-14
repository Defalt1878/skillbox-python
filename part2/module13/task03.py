import os
from typing import Iterator

print('Задача 3. Пути файлов')


def gen_files_path(to_find: str, start: str = os.path.abspath(os.sep)) -> Iterator[str]:
    to_check = [start]

    while to_check:
        current = to_check.pop()
        yield current
        if current.endswith(to_find):
            return
        if os.path.isfile(current):
            continue
        try:
            for inner in os.listdir(current):
                to_check.append(os.path.abspath(os.path.join(current, inner)))
        except PermissionError:
            pass


for path in gen_files_path("FTP.ico"):
    print(path)
