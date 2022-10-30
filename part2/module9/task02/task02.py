print('Задача 2. Дзен Пайтона')

zen_file = open('zen.txt', 'r')
zen = zen_file.read()
zen_file.close()

reversed_zen = '\n'.join(reversed(zen.split('\n')))

print(reversed_zen)
