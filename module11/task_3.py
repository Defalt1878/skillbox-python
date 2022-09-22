from math import ceil, floor

print('Задача 3. Убийца Steam')

size = int(input('Укажите размер файла для скачивания: '))
speed = int(input('Какова скорость вашего соединения? '))

iterations_count = ceil(size / speed)
downloaded = 0

for second in range(1, iterations_count + 1):
    downloaded = min(downloaded + speed, size)
    print(f'Прошло {second} сек. Скачано {downloaded} из {size} Мб ({floor(downloaded / size * 100)}%)')
