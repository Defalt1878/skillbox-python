print('Задача 4. Товары')

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for good in goods:
    good_infos = store[goods[good]]
    total_quantity = sum([info['quantity'] for info in good_infos])
    total_price = sum([info['quantity'] * info['price'] for info in good_infos])
    print(f'{good} — кол-во: {total_quantity}, стоимость: {total_price:,} р.')
