print('Задача 2. Я стал новым пиратом!')

count = 0

for i in range(10):
    # noinspection SpellCheckingInspection
    if input('Что должен кричать настоящий пират? ') == 'Карамба':
        count += 1

print(count, 'пират(а/ов) в команде.')
