print('Задача 1. Драка')


class Unit:

    def __init__(self, name: str, heath=100, damage=20):
        self.name = name
        self.health = heath
        self.damage = damage

    def get_damage(self, damage: int):
        self.health = max(0, self.health - damage)

    def is_dead(self):
        return self.health == 0


attacker = Unit('Воин 1')
defender = Unit('Воин 2')

while True:
    defender.get_damage(attacker.damage)
    print(f'{attacker.name} нанес {attacker.damage} урона {defender.name}')
    print(f'Здоровье {attacker.name}: {attacker.health}')
    print(f'Здоровье {defender.name}: {defender.health}')
    if defender.is_dead():
        print(f'{defender.name} погиб.')
        print(f'{attacker.name} одержал победу!')
        break

    (attacker, defender) = (defender, attacker)
