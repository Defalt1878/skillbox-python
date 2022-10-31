print('Задача 1. Страшный код')


def remove_all(source: list, value):
    return list(filter(lambda n: n != value, source))


general = [1, 5, 3]
side_1 = [1, 5, 1, 5]
side_2 = [1, 3, 1, 5, 3, 3]

general.extend(side_1)
fives_count = general.count(5)
print('Кол-во цифр 5 при первом объединении:', fives_count)

remove_all(general, 5)

general.extend(side_2)
threes_count = general.count(3)
print('Кол-во цифр 3 при втором объединении:', threes_count)

print('Итоговый список:', general)
