print('Задача 8. Пирамидка')

size = int(input('Введите высоту пирамидки: '))
bottom_size = 1 + 2 * (size - 1)

for i in range(size):
    print(' ' * (size - i - 1), end='')
    print('#' * (2 * i + 1))
