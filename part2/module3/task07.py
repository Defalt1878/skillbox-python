print('Задача 7. Ролики')


def get_max_skating_people(skates_sizes: list[int], legs_sizes: list[int]):
    result = 0
    reverse_sorted_skates = list(sorted(skates_sizes, reverse=True))
    for leg_size in sorted(legs_sizes):
        while len(reverse_sorted_skates) > 0 and reverse_sorted_skates[-1] < leg_size:
            reverse_sorted_skates.pop()

        if len(reverse_sorted_skates) == 0:
            break

        result += 1
        reverse_sorted_skates.pop()

    return result


count = int(input('Кол-во коньков: '))

skates = []
for people_i in range(1, count + 1):
    skates.append(int(input(f'Размер {people_i}-й пары: ')))

count = int(input('\nКол-во людей: '))

people = []
for people_i in range(1, count + 1):
    people.append(int(input(f'Размер ноги {people_i}-го человека: ')))

print('\nНаибольшее кол-во людей, которые могут взять ролики:', get_max_skating_people(skates, people))
