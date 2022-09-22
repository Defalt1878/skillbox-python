print('Задача 9. Игра «Угадай число»')

hidden_number = int(input('Загадайте число: '))
attempts_count = 0

while True:
    guess_number = int(input('Введите число: '))
    attempts_count += 1

    if guess_number == hidden_number:
        break

    if guess_number < hidden_number:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Число больше, чем нужно. Попробуйте ещё раз!')

print('Вы угадали! Число попыток:', attempts_count)
