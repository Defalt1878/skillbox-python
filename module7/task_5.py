print('Задача 5. Факториал')

number = int(input('Введите число: '))

factorial = 1
for num in range(2, number + 1):
    factorial *= num

print('Факториал числа', number, 'равен', factorial)
