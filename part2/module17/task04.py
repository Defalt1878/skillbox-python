from collections import Counter

print('Задача 4. Палиндром: возвращение')


def can_be_poly(source: str):
    return len(list(filter(lambda e: e % 2, Counter(source).values()))) < 2


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
