print('Задача 2. Самое длинное слово')

words = input('Введите строку: ').split()

longest = max(words, key=len)

print('Самое длинное слово:', longest)
print('Длина этого слова:', len(longest))
