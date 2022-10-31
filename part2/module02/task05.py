print('Задача 5. Кино')

films = ['Крепкий орешек', 'Назад в будущее',
         'Таксист', 'Леон', 'Богемская рапсодия',
         'Город грехов', 'Мементо', 'Отступники',
         'Деревня']

favorites = []
count = int(input('Сколько фильмов хотите добавить? '))
for i in range(count):
    film = input('Введите название фильма: ')
    if film in films:
        favorites.append(film)
    else:
        print(f'Ошибка: фильма {film} у нас нет :(')

print('Ваш список любимых фильмов:', ', '.join(favorites))
