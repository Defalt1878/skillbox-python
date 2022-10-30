print('Задача 2. Долги')

debtor_amount = int(input('Введите количество должников: '))
debts_sum = 0

for i in range(0, debtor_amount, 5):
    print('Должник с номером', i)
    debts_sum += int(input('Сколько должны? '))

print('Общая сумма долга:', debts_sum)
