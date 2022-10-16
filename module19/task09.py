print('Задача 9. Родословная')


def get_nesting(pairs: dict):
    result = {(set(pairs.values()) - set(pairs.keys())).pop(): 0}
    for child, parent in pairs.items():
        nesting = 1
        while parent not in result:
            nesting += 1
            parent = pairs[parent]
        result[child] = result[parent] + nesting

    return result


children_parents = dict()

people_count = int(input('Введите количество человек: '))

for pair_i in range(1, people_count):
    pair = input(f'{pair_i}-я пара: ').split()
    children_parents[pair[0]] = pair[1]

people_generations = get_nesting(children_parents)

print('\n«Высота» каждого члена семьи:')
print('\n'.join([f'{person} {people_generations[person]}' for person in sorted(people_generations)]))
