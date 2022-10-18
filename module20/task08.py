print('Задача 8. Контакты 3')

contacts = dict()


def find_contacts(surname: str, name: str = None):
    return [
        contact for contact in contacts.items()
        if contact[0][1] == surname and (name is None or contact[0][0] == name)
    ]


def get_action():
    print('\nВведите номер действия:')
    print(' 1. Добавить контакт')
    print(' 2. Найти человека')
    return input()


def add_contact():
    full_name = input('\nВведите имя и фамилию нового контакта (через пробел): ').split()
    if find_contacts(full_name[1], full_name[0]):
        print('Такой человек уже есть в контактах.')
        return
    number = int(input('Введите номер телефона: '))
    contacts[(full_name[0], full_name[1])] = number


def find_contact():
    surname = input('\nВведите фамилию для поиска: ')
    result = find_contacts(surname)
    if len(result) == 0:
        print('Не найдено ни одного контакта с такой фамилией.')
        return
    result = '\n'.join([f'{contact[0][0]} {contact[0][1]} {contact[1]}' for contact in result])
    print(result)


while True:
    action = get_action()
    if action == '1':
        add_contact()
        print('Текущий словарь контактов:', contacts)
    elif action == '2':
        find_contact()
    else:
        print('Ниче не понял.')
