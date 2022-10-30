print('Задача 8. Часы')

hour_angle = float(input('Введите угол на который повернулась часовая стрелка (в градусах): '))
minute_angle = hour_angle % 30 * 12
print(f'Минутная стрелка повернулась на {minute_angle:0.2f} градусов.')
