print('Задача 5. Счастливый билетик')

ticket_number = int(input('Введите номер билета: '))

numbers_count = 0
temp = ticket_number
while temp > 0:
    temp //= 10
    numbers_count += 1

middle = numbers_count // 2
first_half_sum = 0
second_half_sum = 0

temp = ticket_number
i = 0
while temp > 0:
    digit = temp % 10
    temp //= 10
    if i < middle:
        first_half_sum += digit
    else:
        second_half_sum += digit
    i += 1

if first_half_sum == second_half_sum:
    print('Билет счастливый.')
else:
    print('Билет не счастливый.')
