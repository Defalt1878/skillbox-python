print('Задача 5. Марсоход 2')

height = 15
width = 20

x = 8
y = 10

while True:
    print(f'[Программа]: Марсоход находится на позиции {x}, {y}, введите команду:')
    direction = input('[Оператор]: ')
    if direction == 'A':
        if x > 1:
            x -= 1
    elif direction == 'D':
        if x < width:
            x += 1
    elif direction == 'W':
        if y > 1:
            y -= 1
    elif direction == 'S':
        if y < height:
            y += 1
    else:
        break
