print('Задача 7. Пицца')

orders = dict()

orders_count = int(input('Введите количество заказов: '))

for order_i in range(1, orders_count + 1):
    order = input(f'{order_i}-й заказ: ').split()
    name = order[0]
    pizza = order[1]
    count = int(order[2])

    if name not in orders:
        orders[name] = {}

    orders[name][pizza] = orders[name].get(pizza, 0) + count

for person, pizza_count in orders.items():
    print(f'{person}:')
    for pizza, count in pizza_count.items():
        print(' ' * 5 + f'{pizza}: {count}')
