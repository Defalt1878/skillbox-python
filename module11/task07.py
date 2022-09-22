print('Задача 7. Ход конём')

print('Введите местоположение коня:')
horse_x = float(input())
horse_y = float(input())
print('Введите местоположение точки на доске:')
point_x = float(input())
point_y = float(input())

if any(filter(lambda coord: coord < 0 or coord > 0.8, {horse_x, horse_y, point_x, point_y})):
    print('Неверный ввод!')
    quit()

horse_x = int(horse_x * 10)
horse_y = int(horse_y * 10)
point_x = int(point_x * 10)
point_y = int(point_y * 10)

print(f'Конь в клетке ({horse_x}, {horse_y}). Точка в клетке ({point_x}, {point_y}).')

if abs(horse_x - point_x) * abs(horse_y - point_y) == 2:
    print('Да, конь может ходить в эту точку.')
else:
    print('Нет, конь не может ходить в эту точку.')
