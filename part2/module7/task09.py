print('Задача 9. Протокол соревнований')

attendees_scores = {}

count = int(input('Сколько записей вносится в протокол? '))


def parse_record(record_data):
    name = record_data[1]
    score = int(record_data[0])
    if attendees_scores.get(name, (0, 0))[0] < score:
        attendees_scores[name] = score, record_i


def get_winners():
    return [name for name, result
            in sorted(attendees_scores.items(), key=lambda kvp: (kvp[1][0], -kvp[1][1]), reverse=True)
            ][:3]


for record_i in range(1, count + 1):
    record = input(f'{record_i}-я запись: ').split()
    parse_record(record)

print('\nИтоги соревнований:')
for i, winner in enumerate(get_winners()):
    print(f'{i + 1}-е место. {winner} ({attendees_scores[winner][0]})')
