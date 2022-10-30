print('Задача 10.')

cards_amount = int(input('Введите количество карточек: '))
cards_sum = (1 + cards_amount) * cards_amount // 2

for i in range(cards_amount - 1):
    cards_sum -= int(input('Введите номер карточки: '))

print('Потерялась карточка под номером', cards_sum)
