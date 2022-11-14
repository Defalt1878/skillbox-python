from typing import Iterator

print('Задача 1. Квадраты чисел')


class NumbersSquares:
    def __init__(self, count: int):
        self.count = count
        self.current = 0

    def __next__(self) -> int:
        self.current += 1
        if self.current > self.count:
            raise StopIteration
        return self.current ** 2

    def __iter__(self) -> Iterator[int]:
        return self


def number_squares(count: int) -> Iterator[int]:
    for number in range(1, count + 1):
        yield number ** 2


print(list(NumbersSquares(10)))
print(list(number_squares(10)))
print(list((number ** 2 for number in range(1, 11))))
