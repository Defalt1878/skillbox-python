print('Задача 8. Считалка')

attendees_count = int(input('Кол-во человек: '))
counter = int(input('Какое число в считалке? '))
print(f'Значит выбывает каждый {counter}-й человек')

attendees = list(range(1, attendees_count + 1))
count_start = 0

while len(attendees) > 1:
    print('\nТекущий круг людей:', attendees)
    print('Начало с номера', attendees[count_start])

    dropout = (count_start + counter - 1) % len(attendees)
    print('Выбывает человек под номером', attendees[dropout])

    attendees.pop(dropout)
    count_start = dropout % len(attendees)

print('\nОстался человек под номером', attendees[0])
