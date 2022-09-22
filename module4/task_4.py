print('Задача 4. Калькулятор скидки')

totalCost = int(input('Введите стоимость первого товара: '))
totalCost += int(input('Введите стоимость второго товара: '))
totalCost += int(input('Введите стоимость третьего товара: '))

if totalCost > 10_000:
    totalCost *= 0.9
print('Итоговая стоимость:', totalCost)
