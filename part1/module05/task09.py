print('Задача 9. Прогрессивный налог 2')

income = int(input('Введите доход: '))
tax = min(income, 10000) * 0.13

if income > 10000:
    tax += (min(income, 50000) - 10000) * 0.2
    if income > 50000:
        tax += (income - 50000) * 0.3

print('Сумма налога на доход:', tax)
