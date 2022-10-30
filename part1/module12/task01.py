print('Задача 1. Сумма чисел')


def summa_n(n):
    result = (n + n * n) // 2
    return f'Я знаю, что сумма чисел от 1 до {n} равна {result}'


print(summa_n(int(input('Введите число: '))))
