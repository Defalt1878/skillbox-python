print('Задача 4. Поиск элемента 2')

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(key, max_density=None):
    stack = [(site, 0)]
    while stack:
        current_dic, current_density = stack.pop()
        if max_density is not None and current_density >= max_density:
            continue
        if key in current_dic:
            return current_dic[key]
        for value in current_dic.values():
            if isinstance(value, dict):
                stack.append((value, current_density + 1))


key_to_find = input('Введите искомый ключ: ')
if input('Хотите ввести максимальную глубину? Y/N: ') == 'y':
    result = find_key(key_to_find, int(input('Введите максимальную глубину: ')))
else:
    result = find_key(key_to_find)

print('Значение ключа:', result)
