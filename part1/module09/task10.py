print('Задача 10. Метод бутерброда')

encrypted_message = input('Введите зашифрованное сообщение: ')
left_part = ' '
right_part = ' '

for i in range(len(encrypted_message)):
    if i % 2 == 0:
        left_part += encrypted_message[i]
    else:
        right_part = encrypted_message[i] + right_part

print('Расшифрованное сообщение:', left_part + right_part)
