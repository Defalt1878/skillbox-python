import random

print('Задача 9. Недоделка')

rock_paper_scissors_choices = ['камень', 'ножницы', 'бумага']


def winner_index(first_payer_choice, second_player_choice):
    if first_payer_choice == second_player_choice:
        return 0

    first_payer_choice = rock_paper_scissors_choices.index(first_payer_choice)
    second_player_choice = rock_paper_scissors_choices.index(second_player_choice)

    return 1 if (first_payer_choice + 1) % len(rock_paper_scissors_choices) == second_player_choice else 2


def rock_paper_scissors():
    user_action = input(f"\nСделайте выбор ({', '.join(rock_paper_scissors_choices)}): ").lower()
    while not (user_action in rock_paper_scissors_choices):
        print('Ошибка ввода!')
        user_action = input(f"Сделайте выбор ({', '.join(rock_paper_scissors_choices)}): ").lower()

    computer_action = random.choice(rock_paper_scissors_choices)

    print(f'\nВы выбрали {user_action}, компьютер выбрал {computer_action}.')

    match winner_index(user_action, computer_action):
        case 0:
            print('Ничья!')
        case 1:
            print('Вы победили!')
        case 2:
            print('Вы проиграли!')


def guess_the_number(min: int, max: int):
    number = random.randint(min, max)
    trying = 0

    while True:
        print(f'\nЗагадано число от {min} до {max}.')
        user_number = int(input(f'Введите ваш вариант числа: '))
        trying += 1
        if user_number > number:
            print('Число больше, чем нужно. Попробуйте ещё раз!')
        elif user_number < number:
            print('Число меньше, чем нужно. Попробуйте ещё раз!')
        else:
            break

    print(f'\nВы угадали! Число попыток: {trying}')


def main_menu():
    print('В какую игру вы хотите сыграть?')
    print('1 - Камень, ножницы, бумага')
    print('2 - Угадай число\n')
    game = input('Ваш выбор: ')
    if game == '1':
        rock_paper_scissors()
    elif game == '2':
        guess_the_number(1, 100)
    else:
        print('Нет такой игры')


main_menu()
