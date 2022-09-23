print('Задача 8. Сумма ряда')


def calc_row_sum(x: float, precision: float):
    if precision <= 0:
        print('Ошибка ввода!')
        return 0

    result = last_fraction = 1
    n = 0
    while abs(last_fraction) > precision:
        last_fraction *= -x * x
        last_fraction /= (n + 1) * (n + 2)
        n += 2
        result += last_fraction

    return result


precision = float(input("Введите точность: "))
x = int(input("Введите икс: "))

print("Сумма ряда =", calc_row_sum(x, precision))
