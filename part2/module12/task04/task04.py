from Employees import *

print('Задача 4. Компания')

employees = [
    Manager('Вася', 'Пупкин', 67),
    Manager('Жора', 'Жорин', 55),
    Manager('Кузя', 'Изунивера', 25),
    Agent('Николай', 'Петрович', 15, 40000),
    Agent('Пётр', 'Первый', 99, 80000),
    Agent('Агент', 'Просто', 34, 17000),
    Worker('Виктор', 'Работяга', 45, 250),
    Worker('Шкед', 'Среднестатистический', 14, 146),
    Worker('Работник', 'Рабочий', 34, 180),
]

print('\n'.join([str(employee) for employee in employees]))
