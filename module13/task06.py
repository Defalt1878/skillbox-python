print('Задача 6. Маятник ')

start = float(input('Введите начальную амплитуду: '))
while start < 10e-15:
    print('Ошибка ввода!')
    start = float(input('Введите начальную амплитуду: '))

end = float(input('Введите амплитуду остановки: '))
while end < 10e-15:
    print('Ошибка ввода!')
    end = float(input('Введите амплитуду остановки: '))

count = 0

while start > end:
    start *= 0.916
    count += 1

print('Маятник считается остановившимся через', count, 'колебаний')
