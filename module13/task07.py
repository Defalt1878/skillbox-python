print('Задача 7. Яйца')


def get_danger(depth: float):
    return depth ** 3 - 3 * depth ** 2 - 12 * depth + 10


def get_depth(min_depth: float, max_depth: float, danger_delta: float):
    depth = (max_depth + min_depth) / 2
    danger = get_danger(depth)
    while abs(danger) > danger_delta:
        if danger > 0:
            min_depth = depth
        else:
            max_depth = depth

        depth = (max_depth + min_depth) / 2
        danger = get_danger(depth)

    return depth


danger_delta = float(input('Введите максимально допустимый уровень опасности: '))
while danger_delta <= 0:
    print('Ошибка ввода!')
    danger_delta = float(input('Введите максимально допустимый уровень опасности: '))

print('Приблизительная глубина безопасной кладки:', get_depth(0, 4, danger_delta), 'm')
