import collections

print('Задача 7. Годы')


def three_digits_equals(n: int):
    dic = collections.defaultdict(int)
    for d in str(n):
        dic[d] += 1
    return any(filter(lambda count: count == 3, dic.values()))


start_year = int(input('Введите первый год: '))
end_year = int(input('Введите второй год: '))

print(f'Годы от {start_year} до {end_year} с тремя одинаковыми цифрами:')
for year in range(start_year, end_year + 1):
    if three_digits_equals(year):
        print(year)
