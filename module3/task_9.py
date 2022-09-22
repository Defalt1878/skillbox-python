print('Задача 9. В обратном порядке')

number = int(input('Введите число: '))

result = 0
result += number % 10 * 1000
result += number % 100 // 10 * 100
result += number % 1000 // 100 * 10
result += number // 1000

print(result)
