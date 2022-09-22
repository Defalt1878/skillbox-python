print('Задача 7. Стипендия')

educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))

total_money_needed = expenses * (1.03 ** 10 - 1) / 0.03
missing_money = total_money_needed - educational_grant * 10

print(f'У родителей необходимо попросить {missing_money:0.3f}')
