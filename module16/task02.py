print('Задача 2. Шеренга')

first_class = list(range(160, 176 + 1, 2))
second_class = list(range(162, 180 + 1, 3))

sorted_union = sorted(first_class + second_class)

print('Отсортированный список учеников:', sorted_union)
