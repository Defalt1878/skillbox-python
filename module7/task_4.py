print('Задача 4. С заботой о природе')

violations_count = 0
for sector in range(30, 36):
    if int(input(f'Людей в {sector}-м секторе: ')) > 10:
        print('Нарушение! Слишком много людей в секторе!')
        violations_count += 1
    else:
        print('Всё спокойно.')

print('Количество нарушений:', violations_count)
