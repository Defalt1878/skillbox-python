import random

print('Задача 2. Координаты')


def add_f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def subtract_f(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    with open('coordinates.txt', 'r') as source_file, open('result.txt', 'w') as result_file:
        for coords_line in source_file:
            coords = coords_line.split()
            coords = (int(coords[0]), int(coords[1]))

            try:
                add_func_result = add_f(coords[0], coords[1])
            except ArithmeticError:
                print('Что-то пошло не так с первой функцией')
                continue

            try:
                subtract_func_result = subtract_f(coords[0], coords[1])
            except ArithmeticError:
                print('Что-то пошло не так со второй функцией')
                continue

            random_result = random.randint(0, 100)

            sorted_results = sorted([str(add_func_result), str(subtract_func_result), str(random_result)])
            result_file.write(' '.join(sorted_results) + '\n')

except Exception:
    print("Что-то пошло не так:")
