from math import pi

print('Задача 5. Вот это объёмы!')
EARTH_VOLUME = 10.8321 * 10 ** 11

radius = float(input('Введите радиус случайной планеты: '))
volume = 4 / 3 * pi * radius ** 3

if EARTH_VOLUME >= volume:
    print(f'Объём планеты Земля больше в {EARTH_VOLUME / volume:0.3f} раз')
else:
    print(f'Объём планеты Земля меньше в (1/{EARTH_VOLUME / volume:0.3f}) = {volume / EARTH_VOLUME:0.3f} раз')
