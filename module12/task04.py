print('Задача 4. Число наоборот')


def reverse(source_number: int):
    return str(abs(source_number))[::-1]


while True:
    number = int(input('Введите число: '))
    if number == 0:
        print('Программа завершена!')
        break
    print('Число наоборот:', reverse(number), end='\n\n')
