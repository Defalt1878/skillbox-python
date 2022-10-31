print('Задача 3. Сумма и разность')


def digits(n: int):
    return list(map(int, str(n)))


def digits_count(n: int):
    return len(digits(n))


def digits_sum(n: int):
    return d_sum(digits(n))


number = int(input('Введите число: '))

d_sum = digits_sum(number)
d_count = digits_count(number)

print('Сумма цифр:', d_sum)
print('Количество цифр в числе', d_count)
print('Разность суммы и количества цифр:', d_sum - d_count)
