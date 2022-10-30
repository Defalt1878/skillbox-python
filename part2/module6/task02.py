print('Задача 2. География')

cities = dict()
count = int(input('Количество стран: '))

for city_i in range(1, count + 1):
    country_cities = input(f'{city_i}-я страна: ').split()
    cities.update({city: country_cities[0] for city in country_cities[1:]})

for city_i in range(1, 4):
    city = input(f'\n{city_i}-й город: ')
    if city in cities:
        print(f'Город {city} расположен в стране {cities[city]}')
    else:
        print(f'По городу {city} данных нет.')
