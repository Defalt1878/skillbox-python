print('Задача 4. Число наоборот 3')


def reverse_integer_part(n: float):
    tokens = str(n).split('.')
    integer_reversed = tokens[0][::-1]
    fractional_reversed = tokens[1][::-1]
    result = integer_reversed + '.' + fractional_reversed
    return float(result)


first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))

first_r = reverse_integer_part(first)
second_r = reverse_integer_part(second)

print('Первое число наоборот:', first_r)
print('Второе число наоборот:', second_r)
print('Сумма:', first_r + second_r)
