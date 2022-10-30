import random

print('Задача 3. Случайные соревнования')

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]

winners = [(first_team[score]
            if first_team[score] > second_team[score]
            else second_team[score])
           for score in range(20)]

print('Первая команда:', first_team)
print('Вторая  команда:', second_team)
print('Победители тура:', winners)
