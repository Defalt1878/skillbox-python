print('Задача 7. IP-адрес 2')


def get_ip_check_result(_ip: str):
    ip_parts = _ip.split('.')
    if len(ip_parts) != 4:
        return 'Адрес — это четыре числа, разделённые точками.'

    not_integer_parts = [part for part in ip_parts if not part.isnumeric()]
    if len(not_integer_parts) > 0:
        return '\n'.join([f'{part} — это не целое число.' for part in not_integer_parts])

    wrong_int_parts = [part for part in ip_parts if int(part) > 255]
    if len(wrong_int_parts) > 0:
        return '\n'.join([f'{part} превышает 255.' for part in wrong_int_parts])

    return 'IP-адрес корректен.'


ip = input('Введите IP: ')
print(get_ip_check_result(ip))
