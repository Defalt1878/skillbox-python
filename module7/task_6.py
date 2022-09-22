print('Задача 6. Успеваемость в классе')

number_people = int(input('Сколько человек в классе? '))
three_count = 0
four_count = 0
five_count = 0

for i in range(number_people):
    grade = int(input('Введите оценку: '))
    if grade == 3:
        three_count += 1
    elif grade == 4:
        four_count += 1
    else:
        five_count += 1

if five_count > four_count and five_count > three_count:
    print('Сегодня больше отличников.')
elif four_count > three_count:
    print('Сегодня больше хорошистов.')
else:
    print('Сегодня больше троечников.')
