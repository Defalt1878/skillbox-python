print('Задача 7. Турнир')


def format_attendee(name, surname, score):
    return f'{name[0]}. {surname} {score}'


def get_second_tour_attendees(min_score: int, attendees: list[str]):
    result = []
    for attendee in attendees:
        parts = attendee.split()
        score = int(parts[2])
        if score > min_score:
            result.append((parts[0], parts[1], score))

    result.sort(reverse=True, key=lambda tpl: tpl[2])
    return [format_attendee(attendee[1], attendee[0], attendee[2]) for attendee in result]


first_tour_file = open('first_tour.txt')
data = first_tour_file.read()
print('\nСодержимое файла first_tour.txt:')
print(data)
data = data.split('\n')
second_tour_attendees = get_second_tour_attendees(int(data[0]), data[1:])
first_tour_file.close()

second_tour_info = [str(len(second_tour_attendees))]
for i, attendee in enumerate(second_tour_attendees):
    second_tour_info.append(f'{i + 1}) {attendee}')
second_tour_info = '\n'.join(second_tour_info)

second_tour_file = open('second_tour.txt', 'w')
second_tour_file.write(second_tour_info)
second_tour_file.close()

print('\nСодержимое файла second_tour.txt:')
print(second_tour_info)
