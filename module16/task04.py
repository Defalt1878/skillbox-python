print('Задача 4. Вечеринка')

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    ans = input('Гость пришёл или ушёл? ')
    if ans == 'Пора спать':
        break
    if ans != 'пришёл' and ans != 'ушёл':
        print('Ниче не понял.\n')
        continue

    guest = input('Имя гостя: ')
    if ans == 'пришёл':
        if len(guests) < 6:
            guests.append(guest)
            print(f'Привет, {guest}!')
        else:
            print(f'Прости, {guest}, но мест нет.')
    else:
        if guest in guests:
            guests.remove(guest)
            print(f'Пока, {guest}!')
        else:
            print('Его тут и не было.')
    print()

print('\nВечеринка закончилась, все легли спать.')
