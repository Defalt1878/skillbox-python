print('Задача 5. Разворот')

string = input('Введите строку: ')

first_h_i = string.index('h')
last_h_i = len(string) - 1 - string[::-1].index('h')

result = string[last_h_i - 1:first_h_i:-1]
print('Развёрнутая последовательность между первым и последним h:', result)
