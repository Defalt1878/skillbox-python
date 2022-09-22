print('Задача 1. Калькулятор опыта')

exp = int(input('Введите количество опыта: '))

if exp > 5000:
    level = 4
elif exp > 2500:
    level = 3
elif exp > 1000:
    level = 2
else:
    level = 1
print('Ваш уровень:', level)
