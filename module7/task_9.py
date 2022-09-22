print('Задача 9. ...Теперь можно посчитать и свою')

previous_salary = 0
isIncreasing = True

for month in range(1, 11):
    salary = int(input(f'Введите зарплату за месяц {month}: '))
    if salary <= previous_salary:
        isIncreasing = False
    previous_salary = salary

if isIncreasing:
    print('Зарплата все время увеличивалась.')
else:
    print('Зарплата увеличивалась не каждый месяц.')
