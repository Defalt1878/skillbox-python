import random

from KarmaErrors import KARMA_ERRORS, KarmaError

print('Задача 2. Карма')


def one_day():
    if random.randint(1, 10) == 1:
        raise random.choice(KARMA_ERRORS)
    return random.randint(1, 7)


KARMA_NEEDED = 500

karma_collected = 0
day = 1

with open('karma.log', 'w', encoding='utf-8') as log:
    while karma_collected < KARMA_NEEDED:
        try:
            karma_collected += one_day()
        except KarmaError as e:
            log.write(f'День {day}: {e}\n')
        day += 1

print(f'Вы успешно накопили {KARMA_NEEDED} кармы за {day} дней.')
