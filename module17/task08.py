print('Задача 8. Развлечение')

sticks_count = int(input('Количество палок: '))
throws_count = int(input('Количество бросков: '))
sticks = [True] * sticks_count

for throw in range(1, throws_count + 1):
    left = int(input(f'Бросок {throw}. Сбиты палки с номера '))
    right = int(input('по номер '))
    sticks[left - 1:right] = [False] * (right - left + 1)

result_answer = ''.join(['|' if stick_condition else '.' for stick_condition in sticks])
print('\nРезультат:', result_answer)
