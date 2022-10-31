print('Задача 5. Наименьший делитель')


def least_divisor(n: int):
    if n % 2 == 0:
        return 2

    max_i = int(n ** 0.5)
    for i in range(3, max_i + 1, 2):
        if n % i == 0:
            return i

    return n


number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', least_divisor(number))
