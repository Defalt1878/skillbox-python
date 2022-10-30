print('Задача 9. Список списков')


def flat_map(source: list[list]):
    return [nested_e for nested in source for nested_e in nested]


nice_list = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
]

print('Исходный лист:', nice_list)

result = flat_map(nice_list)
print('Лист после первого раскрытия:', result)

result = flat_map(result)
print('Ответ:', result)
