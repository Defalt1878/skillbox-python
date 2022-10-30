print('Задача 6. Игра в кубики')

# noinspection SpellCheckingInspection
kostya_dice = int(input('Кубик Кости: '))
owner_dice = int(input('Кубик владельца: '))

if kostya_dice >= owner_dice:
    print('Разность:', kostya_dice - owner_dice)
    print('Костя платит')
else:
    print('Сумма:', kostya_dice + owner_dice)
    print('Владелец платит')

print('Игра окончена')
