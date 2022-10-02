print('Задача 4. Видеокарты')


def get_without_max(source: list):
    max_element = max(source)
    return [e for e in source if e != max_element]


cards = []

count = int(input('Количество видеокарт: '))
for card in range(1, count + 1):
    cards.append(int(input(f'{card} видеокарта: ')))

print('Старый список видеокарт:', cards)
print('Новый список видеокарт:', get_without_max(cards))
