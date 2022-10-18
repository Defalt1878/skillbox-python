print('Задача 4. Игроки')

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}


def concat_keys_values(source: dict[tuple, tuple]):
    return [key + value for key, value in source.items()]


print(concat_keys_values(players))
