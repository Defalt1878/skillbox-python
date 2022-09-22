print('Задача 8. Колонтитул')

header_length = int(input('Введите общую длину колонтитула: '))
exclamation_count = int(input('Введите количество восклицательных знаков: '))

tilde_count = header_length - exclamation_count
if tilde_count % 2 != 0:
    print('Ровный колонтитул не получится!')
    quit()

print('~' * (tilde_count // 2), end='')
print('!' * exclamation_count, end='')
print('~' * (tilde_count // 2), end='')
