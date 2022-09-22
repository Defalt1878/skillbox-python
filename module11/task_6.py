print('Задача 6. Метеостанция')

print('Ввод:')
lower = int(input('Нижняя граница: '))
higher = int(input('Верхняя граница: '))
step = int(input('Шаг: '))

if lower > higher or step <= 0:
    print('Ошибка ввода')
    quit()

print('\nВывод:')
print('C\tF')

for degree in range(lower, higher, step):
    print(f'{degree}\t{32 + degree * 1.8:0.0f}')

print(f'{higher}\t{32 + higher * 1.8:0.0f}')
