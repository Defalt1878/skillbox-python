print('Задача 7. Поездка по кругу')

v = int(input('Введите скорость (км/ч): '))
t = int(input('Введите время (ч): '))

print(f'Ответ: {(v * t) % 115} км')
