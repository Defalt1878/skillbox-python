print('Задача 2. Рефакторинг')


def cross_intersect(first_list: list, second_list: list):
    for x in first_list:
        for y in second_list:
            yield x, y


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

for number_1, number_2 in cross_intersect(list_1, list_2):
    print(f'{number_1} * {number_2} = {number_1 * number_2}')
    if number_1 * number_2 == to_find:
        print('Found!!!')
        break
