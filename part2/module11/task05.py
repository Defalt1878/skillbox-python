print('Задача 5. Весёлая ферма 2')


class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1

    def is_ripe(self):
        return self.state == 3

    def reap(self):
        self.state = 0

    def __str__(self):
        return f'Картошка {self.index} сейчас {Potato.states[self.state]}'


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        return all([potato.is_ripe() for potato in self.potatoes])


class Gardener:
    def __init__(self, name: str, garden):
        self.name = name
        self.garden = garden

    def take_care_garden(self):
        self.garden.grow()

    def reap_harvest(self):
        ripe_count = 0
        for potato in self.garden.potatoes:
            if not potato.is_ripe():
                continue
            ripe_count += 1
            potato.reap()

        return ripe_count
