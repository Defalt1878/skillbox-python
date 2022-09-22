print('Задача 9. Плохой циферблат')

mileage = int(input('Введите пробег: '))
day = int(input('Введите сегодняшнее число: '))

digitsSum = 0
for digit in str(mileage):
    digitsSum += int(digit)

if digitsSum > day:
    print('Сброс.')
    mileage = 0
else:
    print('Сегодня не сломался.')

print('Пробег:', mileage)
