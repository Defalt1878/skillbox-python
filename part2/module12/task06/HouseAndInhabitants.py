import random


class House:
    def __init__(self, *inhabitants):
        self.__money = 100
        self.__food_amount = 50
        self.__cat_food_amount = 30
        self.__pollution_volume = 0
        self.__inhabitants = list(inhabitants)

    @property
    def people_count(self):
        return len([inhabitant for inhabitant in self.__inhabitants if isinstance(inhabitant, Person)])

    @property
    def cats_count(self):
        return len([inhabitant for inhabitant in self.__inhabitants if isinstance(inhabitant, Cat)])

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value: int):
        if value < 0:
            raise ValueError
        self.__money = value

    @property
    def food_amount(self):
        return self.__food_amount

    @food_amount.setter
    def food_amount(self, value: int):
        if value < 0:
            raise ValueError
        self.__food_amount = value

    @property
    def cat_food_amount(self):
        return self.__cat_food_amount

    @cat_food_amount.setter
    def cat_food_amount(self, value: int):
        if value < 0:
            raise ValueError
        self.__cat_food_amount = value

    @property
    def pollution_volume(self):
        return self.__pollution_volume

    @pollution_volume.setter
    def pollution_volume(self, value: int):
        if value < 0:
            raise ValueError
        self.__pollution_volume = value

    def next_day(self):
        for inhabitant in self.__inhabitants:
            inhabitant.do_action(self)

        self.pollution_volume += 5

    def __str__(self):
        return '\n'.join(
            [
                'Дом:',
                f'\tКол-во денег: {self.money}',
                f'\tКоличество еды: {self.food_amount}',
                f'\tКоличество еды для кота: {self.cat_food_amount}',
                f'\tОбъём загрязнений: {self.pollution_volume}',
            ] + [f'\t{str(inhabitant)}' for inhabitant in self.__inhabitants]
        )


class Inhabitant:
    def __init__(self, name):
        self._name = name
        self._satiety = 30

    @property
    def name(self):
        return self._name

    @property
    def satiety(self):
        return self._satiety

    def eat(self, house: House):
        raise NotImplementedError

    def check_not_dead(self):
        if self.satiety < 0:
            raise DeadError(f'{self._name} умер от голода!')

    def do_action(self, house: House):
        raise NotImplementedError

    def __str__(self):
        return f'{self.name}:\tСытость: {self.satiety}'


class Person(Inhabitant):
    def __init__(self, name):
        super().__init__(name)
        self._happiness = 100

    @property
    def happiness(self):
        return self._happiness

    def eat(self, house: House):
        to_eat = min(house.food_amount, 30)
        if to_eat == 0:
            return False
        self._satiety += to_eat
        house.food_amount -= to_eat
        return True

    def pet_cat(self):
        self._satiety -= 10
        self._happiness += 5
        return True

    def check_not_dead(self):
        super().check_not_dead()
        if self.happiness < 10:
            raise DeadError(f'{self._name} умер от депрессии!')

    def do_action(self, house: House):
        if house.pollution_volume > 90:
            self._happiness -= 10

    def __str__(self):
        return '\t'.join((super().__str__(), f'Счастье: {self.happiness}'))


class Husband(Person):
    def play(self):
        self._satiety -= 10
        self._happiness += 20
        return True

    def work(self, house: House):
        self._satiety -= 10
        house.money += 150
        return True

    def do_action(self, house: House):
        super().do_action(house)
        if self.satiety < 50 and self.eat(house):
            pass
        elif self.happiness < 40:
            self.play()
        elif self.happiness < 60:
            self.pet_cat()
        else:
            self.work(house)
        self.check_not_dead()


class Wife(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__fur_coats_count = 0

    def buy_food(self, house: House):
        to_buy = min(house.money, 50 * house.people_count)
        if to_buy == 0:
            return False
        self._satiety -= 10
        house.food_amount += to_buy
        house.money -= to_buy
        return True

    def buy_cat_food(self, house: House):
        to_buy = min(house.money, 50 * house.cats_count)
        if to_buy == 0:
            return False
        self._satiety -= 10
        house.cat_food_amount += to_buy
        house.money -= to_buy
        return True

    def buy_fur_coat(self, house: House):
        if house.money < 350:
            return False
        self._satiety -= 10
        house.money -= 350
        self.__fur_coats_count += 1
        self._happiness += 60
        return True

    def clean_house(self, house: House):
        to_clean = min(house.pollution_volume, 100)
        if to_clean == 0:
            return False
        self._satiety -= 10
        house.pollution_volume -= to_clean
        return True

    def do_action(self, house: House):
        super().do_action(house)
        if self.satiety < 50 and self.eat(house):
            pass
        elif self.happiness < 30 and self.buy_fur_coat(house):
            pass
        elif self.happiness < 60:
            self.pet_cat()
        elif house.food_amount < 30 * house.people_count and self.buy_food(house):
            pass
        elif house.cat_food_amount < 30 * house.cats_count and self.buy_cat_food(house):
            pass
        elif house.pollution_volume > 80:
            self.clean_house(house)
        if self.satiety < 60 and self.eat(house):
            pass
        if house.money > 1000 and self.__fur_coats_count < 20:
            self.buy_fur_coat(house)
        else:
            self.pet_cat()
        self.check_not_dead()

    def __str__(self):
        return '\t'.join((super().__str__(), f'Число шуб: {self.__fur_coats_count}'))


class Child(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__phones_count = 0

    def play(self):
        self._satiety -= 10
        self._happiness += 20
        return True

    def foul(self, house):
        self._satiety -= 10
        house.pollution_volume += 5

    def turn_penny(self, house):
        self._satiety -= 10
        self._happiness -= 5
        house.money += 50

    def buy_phone(self, house):
        if house.money < 200:
            return False
        self._satiety -= 10
        house.money -= 200
        self.__phones_count += 1
        self._happiness += 50
        return True

    def steal_money(self, house):
        to_steal = min(house.money, 50)
        if to_steal == 0:
            return False
        self._satiety -= 10
        house.money -= 50
        self._happiness += 20

    def do_action(self, house: House):
        super().do_action(house)
        if self.satiety < 50 and self.eat(house):
            pass
        elif self.happiness < 60:
            self.play()
        elif house.money > 1000 and self.__phones_count < 10:
            self.buy_phone(house)
        else:
            rnd = random.randint(1, 3)
            if rnd == 1 and self.steal_money(house):
                pass
            elif rnd == 2:
                self.foul(house)
            else:
                self.turn_penny(house)
        self.check_not_dead()

    def __str__(self):
        return '\t'.join((super().__str__(), f'Число телефонов: {self.__phones_count}'))


class Cat(Inhabitant):
    def eat(self, house: House):
        to_eat = min(house.cat_food_amount, 10)
        if to_eat == 0:
            return False
        self._satiety += 2 * to_eat
        house.cat_food_amount -= to_eat
        return True

    def sleep(self):
        self._satiety -= 10
        return True

    def tear_wallpaper(self, house: House):
        self._satiety -= 10
        house.pollution_volume += 5
        return True

    def do_action(self, house: House):
        if self.satiety < 50 and self.eat(house):
            pass
        else:
            if random.randint(1, 5) == 1:
                self.tear_wallpaper(house)
            else:
                self.sleep()
        self.check_not_dead()


class DeadError(RuntimeError):
    pass
