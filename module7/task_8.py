print('Задача 8. Замечательные числа')

for number in range(10, 100):
    if ((number % 10) * (number // 10) * 3) == number:
        print(number)
