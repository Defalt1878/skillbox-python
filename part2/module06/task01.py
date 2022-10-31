print('Задача 1. Песни 2')

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

total_time = 0
count = int(input('Сколько песен выбрать? '))

song_i = 1
while song_i <= count:
    song = input(f'Название {song_i}-й песни: ')
    if song not in violator_songs:
        print('Нет такой песни в списке.')
        continue
    total_time += violator_songs[song]
    song_i += 1

print(f'\nОбщее время звучания песен: {total_time:.2f} минуты')
