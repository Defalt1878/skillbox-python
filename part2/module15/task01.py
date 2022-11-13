import io
from typing import TextIO

print('Задача 1. Работа с файлом 2')


class File:
    def __init__(self, name: str, encoding='utf-8'):
        self.file = None
        self.path = name
        self.encoding = encoding

    def __enter__(self) -> TextIO:
        self.file = open(self.path, 'w', encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        if exc_type is io.UnsupportedOperation:
            print('Подавлено исключение:', repr(exc_val))
            return True


with File("test.txt") as file:
    file.write('123')
    file.read()
