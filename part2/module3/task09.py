print('Задача 9. Друзья')

friends_count = int(input('Кол-во друзей: '))
ious_count = int(input('Долговых расписок: '))

balance_sheets = [0] * friends_count

for iou in range(1, ious_count + 1):
    print(f'\n{iou}-я расписка')
    iou_to = int(input('Кому: '))
    iou_from = int(input('От кого: '))
    amount = int(input('Сколько: '))

    balance_sheets[iou_to - 1] -= amount
    balance_sheets[iou_from - 1] += amount

print('\nБаланс друзей:')
for balance_i in range(friends_count):
    print(f'{balance_i + 1}: {balance_sheets[balance_i]}')
