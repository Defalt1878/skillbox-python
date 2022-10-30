print('Задача 10. Игра «Компьютер угадывает число»')

hidden_number = int(input('Загадайте число от 1 до 100: '))

left_border = 1
right_border = 100

while True:
    middle = (left_border + right_border) // 2
    print(f'Твое число больше, меньше или равно {middle}?')
    result = int(input('Введите ответ (1 — равно, 2 — больше, 3 — меньше): '))

    if result == 1:
        break

    if result == 2:
        left_border = middle + 1
    elif result == 3:
        right_border = middle
    else:
        # noinspection SpellCheckingInspection
        print('Ниче не понял.')

print('Твое число', middle)
print('Спасибо за игру.')
