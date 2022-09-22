print('Задача 7. Обычный день на работе')

tasks_completed = 0
call_accepted = False

print('Начался 8-часовой рабочий день.')

hour = 0
while hour < 8:
    hour += 1
    print(f'{hour}-й час')
    tasks_completed += int(input('Сколько задач решит Максим? '))
    if input('Звонит жена. Взять трубку? (1 — да, 0 — нет): ') == '1':
        call_accepted = True

print('Рабочий день закончился. Всего выполнено задач:', tasks_completed)
if call_accepted:
    print('Нужно зайти в магазин.')
