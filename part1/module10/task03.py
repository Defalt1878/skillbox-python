print('Задача 3. Рамка')

width = int(input('Введите ширину рамки: '))
height = int(input('Введите высоту рамки: '))

middle_line = '|' + ' ' * (width - 2) + '|'

print('|' + '-' * (width - 2) + '|')
for row in range(height - 2):
    print(middle_line)
print('|' + '-' * (width - 2) + '|')
