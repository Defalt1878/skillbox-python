from typing import TextIO

print('Задача 6. Чат')

MESSAGE_PATTERN = "'{}': '{}'\n"


def get_user_action():
    print('\nВыберите одно из действий:')
    print('\t 1. Посмотреть текущий текст чата.')
    print('\t 2. Отправить сообщение.')
    print('\t 3. Выход.')
    return input('Введите номер действия (число 1, 2 или 3): ')


def print_chat(_chat: TextIO):
    print('\nПредыдущие сообщения чата:\n')
    _chat.seek(0)
    print(_chat.read())


def new_message(username: str, _chat: TextIO):
    message = input('Введите сообщение: ')
    _chat.write(MESSAGE_PATTERN.format(username, message))


name = input('Введите ваше имя: ')

with open('chat.txt', 'a+', encoding='utf-8') as chat:
    while True:
        try:
            match get_user_action():
                case '1':
                    print_chat(chat)
                case '2':
                    new_message(name, chat)
                case '3':
                    break
                case _:
                    print('Нет такой команды. Попробуйте ещё раз.')
        except BlockingIOError:
            print('В текущий момент с чатом работает другой пользователь.')
            print('Подождите немного и повторите попытку.')
