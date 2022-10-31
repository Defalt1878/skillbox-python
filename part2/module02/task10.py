print('Задача 10. Сортировка')

numbers = []

count = int(input('Количество чисел: '))
for e in range(count):
    numbers.append(int(input('Введите число: ')))

print('Изначальный список:', numbers)
print('Отсортированный список:', sorted(numbers))
