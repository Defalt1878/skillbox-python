from HouseAndInhabitants import *

print('Задача 6. Совместное проживание 2')

house = House(
    Husband("Валера"),
    Wife('Надя'),
    Child('Васген'),
    Cat('Борис'),
    Cat('Василий')
)

try:
    for day in range(1, 366):
        print(f'\nДень {day}:')
        print(f'Состояние дома: {house}')
        house.next_day()
except DeadError as e:
    print(e)
else:
    print('\nЖители успешно прожили год!')
