from Properties import *

print('Задача 1. Налоги')

money = float(input('Сколько у вас денег? '))

properties = [
    Apartment(int(input('\nСколько стоит ваша квартира? '))),
    Car(int(input('Сколько стоит ваша машина? '))),
    CountryHouse(int(input('Сколько стоит ваша дача? ')))
]
tax = sum([prop.get_tax() for prop in properties])

print(f'\nОбщая сумма налога: {tax:.2f}')
if tax <= money:
    print('Вам хватает денег.')
else:
    print(f'Для выплаты не хватает: {(tax - money):.2f}')
