print('Задача 6. Поставьте оценку!')

positive_count = 0
negative_count = 0
while True:
    number = int(input('Введите число: '))
    if number == 0:
        break
    if number > 0:
        positive_count += 1
    else:
        negative_count += 1

print('Количество положительных чисел:', positive_count)
print('Количество отрицательных чисел:', negative_count)
