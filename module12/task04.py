print('Задача 4. Число наоборот')


def get_reversed(source_number: int):
    return str(abs(source_number))[::-1]


while True:
    number = int(input('Введите число: '))
    if number == 0:
        print('Программа завершена!')
        break
    print('Число наоборот:', get_reversed(number), end='\n\n')
