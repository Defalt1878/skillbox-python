print('Задача 9. Коровы')
stalls = input('Введите информацию о стойлах (a - свободное, b - занятое): ')
milk_amount = 0

for i in range(len(stalls)):
    if stalls[i] == 'b':
        milk_amount += (i + 1) * 2

print('За день будет произведено молока:', milk_amount, 'л.')
