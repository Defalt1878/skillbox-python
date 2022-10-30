print('Задача 10. Кинотеатр')

boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))

if (boys > 2 * girls) or (girls > 2 * boys):
    print('Ответ: Нет решения')
    quit()

result = ''
coeff = abs(boys - girls)
if boys >= girls:
    triple = 'BGB'
    double = 'BG'
else:
    triple = 'GBG'
    double = 'GB'

for i in range(coeff):
    result += triple
for i in range(min(boys, girls) - coeff):
    result += double

print('Ответ:', result)
