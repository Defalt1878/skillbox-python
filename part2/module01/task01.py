import platform
import sys

print('Задача 1. Информация о системе')

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture(),
)
print(info)

with open('module01/os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)
