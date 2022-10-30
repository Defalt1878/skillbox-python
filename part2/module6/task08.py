print('Задача 8. Угадай число')

max_number = int(input('Введите максимальное число: '))
can_guess = set(range(1, max_number + 1))

while True:
    guess_numbers = input('\nНужное число есть среди вот этих чисел: ')
    if guess_numbers == 'Помогите!':
        break

    guess_numbers = set([int(e) for e in guess_numbers.split()])
    answer = input('Ответ Артёма: ')
    if answer == 'Да':
        can_guess &= guess_numbers
    elif answer == 'Нет':
        can_guess -= guess_numbers
    else:
        print('Ниче не понял.')

print('Артём мог загадать следующие числа:', ' '.join([str(e) for e in can_guess]))
