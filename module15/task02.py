print('Задача 2. Турнир')


def get_even_index_elements(source: list):
    indices = list(range(0, len(source), 2))
    return [source[i] for i in indices]


participants = []

print('Введите имена участников (оставьте строку пустой чтобы закончить.)')
while len(participants) == 0 or participants[-1] != '':
    participants.append(input('Введите имя участника: '))

participants.pop()

print('Все участники:', participants)
print('Первый день:', get_even_index_elements(participants))
