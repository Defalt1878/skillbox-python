print('Задача 5. Одна семья')

names_ages = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Петров', 'Павел'): 7,
    ('Петрова', 'Нина'): 29,
    ('Иванов', 'Иван'): 56,
}


def surnames_equals(first: str, second: str):
    if first.endswith('а'):
        first = first[:-1]
    if second.endswith('а'):
        second = second[:-1]
    return first.lower() == second.lower()


searching_surname = input('Введите фамилию: ')
searching_surname = searching_surname.lower()

for (surname, name), age in names_ages.items():
    if not surnames_equals(searching_surname, surname):
        continue
    print(f'{surname} {name} {age}')
