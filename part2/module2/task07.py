print('Задача 7. Контейнеры')


def get_position_of_new(source: list[int], new: int):
    for i in range(len(source)):
        if new > source[i]:
            return i + 1
    return len(source)


containers = []

count = int(input('Количество контейнеров: '))
for container in range(count):
    weight = int(input('Введите вес контейнера: '))
    if weight > 200:
        print('Ошибка! Вес не должен превышать 200.')
        quit()
    containers.append(weight)

new_weight = int(input('Введите вес нового контейнера: '))

print('Номер, который получит новый контейнер:', get_position_of_new(containers, new_weight))
