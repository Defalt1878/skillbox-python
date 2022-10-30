print('Задача 6. Письмо')
size = int(input('Укажите высоту или ширину письма: '))
folds_count = 0
while size > 12:
    size /= 2
    folds_count += 2
print('Чтобы письмо поместилось в конверт, нужно сложить его', folds_count, 'раз.')
