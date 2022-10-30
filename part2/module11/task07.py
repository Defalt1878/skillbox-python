import random

print('Задача 7. Совместное проживание')


class House:
    def __init__(self):
        self.food_amount = 50
        self.money = 0

    def __str__(self):
        return f'Деньги: {self.money}. Еда: {self.food_amount}'


class Person:
    def __init__(self, name: str, house: House):
        self.name = name
        self.house = house
        self.satiety = 50

    def eat(self, amount: int):
        amount = min(amount, self.house.food_amount)
        if amount == 0:
            return False
        self.satiety += amount
        self.house.food_amount -= amount
        return True

    def work(self, amount: int):
        amount = min(amount, self.satiety)
        if amount == 0:
            return False
        self.house.money += amount
        self.satiety -= amount
        return True

    def play(self, amount: int):
        amount = min(amount, self.satiety)
        self.satiety -= amount

    def buy_food(self, amount: int):
        amount = min(amount, self.house.money)
        if amount == 0:
            return False
        self.house.food_amount += amount
        self.house.money -= amount
        return True

    def is_dead(self):
        return self.satiety == 0

    def do_action(self, amount: int):
        if self.is_dead():
            raise SyntaxError
        if self.satiety < 20 and self.eat(amount):
            return
        if self.house.food_amount < 10 and self.buy_food(amount):
            return
        if self.house.money < 50 and self.work(amount):
            return
        if amount == 1 and self.work(amount):
            return
        if amount == 2 and self.eat(amount):
            return
        self.play(amount)

    def __str__(self):
        return f'{self.name}. Сытость: {self.satiety}'


house = House()
person1 = Person('Валера', house)
person2 = Person('Лена', house)

for day in range(1, 366):
    print(f'\nДень {day}:')
    print(f'Состояние дома: {house}')
    print('Состояние жителей:')
    print(person1)
    print(person2)
    if person1.is_dead() or person2.is_dead():
        if person1.is_dead():
            print(f'{person1.name} умер(-ла). Конец!')
        if person2.is_dead():
            print(f'{person2.name} умер(-ла). Конец!')
        break
    person1.do_action(random.randint(1, 6))
    person2.do_action(random.randint(1, 6))
else:
    print('\nЖители успешно прожили год!')
