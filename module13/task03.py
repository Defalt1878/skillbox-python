print('Задача 3. Число наоборот 2')


def reverse(number: int):
    return int(str(abs(number))[::-1])


n = int(input('Введите первое число: '))
k = int(input('Введите второе число: '))

n_reverse = reverse(n)
k_reverse = reverse(k)

print('\nПервое число наоборот:', n_reverse)
print('Второе число наоборот:', k_reverse)
print('\nСумма:', n + k)
print('Сумма наоборот:', n_reverse + k_reverse)
