print('Задача 8. Бегущая строка')


def get_shift(first: str, second: str):
    if len(first) != len(second):
        return -1

    for i in range(len(first)):
        if second == ''.join([first[i:], first[:i]]):
            return i
    return -1


first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')

shift = get_shift(first_str, second_str)
if shift == -1:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    print(f'Первая строка получается из второй со сдвигом {shift}.')
