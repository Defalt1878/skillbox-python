import itertools

print('Задача 5. ПИН-код')

for pin_code in itertools.product(range(10), repeat=4):
    print(*pin_code)
