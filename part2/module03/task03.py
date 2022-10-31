print('Задача 3. Детали')

shop = [
    ['каретка', 1200], ['шатун', 1000], ['седло', 300],
    ['педаль', 100], ['седло', 1500], ['рама', 12000],
    ['обод', 2000], ['шатун', 200], ['седло', 2700]
]

detail = input('Название детали: ')

count = 0
cost = 0

for detail_count in shop:
    if detail_count[0] == detail:
        count += 1
        cost += detail_count[1]

print('Кол-во деталей —', count)
print('Общая стоимость —', cost)
