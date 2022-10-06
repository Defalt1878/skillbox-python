print('Задача 6. Уникальные элементы')


def get_input_list(count: int, list_number):
    return list(map(
        lambda i: int(input(f'Введите {i}-е число для {list_number}-го списка: ')),
        range(1, count + 1)
    ))


def distinct_start(source: list):
    # В задании запретили использовать условный оператор и set, поэтому используем костыли)
    result = []
    for e in reversed(source):
        try:
            result.index(e)
        except ValueError:
            result.append(e)

    result.reverse()
    return result


list_1 = get_input_list(3, 1)
list_2 = get_input_list(7, 2)

print('Первый список:', list_1)
print('Второй список:', list_2)

list_1.extend(list_2)
list_1 = distinct_start(list_1)

print('Новый первый список с уникальными элементами: ', list_1)
