print('Задача 1. Урок информатики 2')

number = float(input("Введите число: "))
if number <= 0:
    print('Некорректный ввод.')
    quit()

degree = 0

while number < 1:
    number *= 10
    degree -= 1

while number >= 10:
    number /= 10
    degree += 1

print(f"Формат плавающей точки: x = {number} * 10 ** {degree}")
