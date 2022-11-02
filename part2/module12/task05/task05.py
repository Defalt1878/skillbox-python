import math
from math import radians

print('Задача 5. А-а-автомобиль!')


class Car:
    def __init__(self, x: float, y: float, angle_in_degrees: float):
        self.__x = x
        self.__y = y
        self.__angle = None
        self.set_angle(angle_in_degrees)

    def get_position(self):
        return self.__x, self.__y

    def get_angle(self):
        return self.__angle

    def set_angle(self, angle_in_degrees):
        angle_in_degrees %= 360
        if angle_in_degrees > 180:
            angle_in_degrees -= 360
        self.__angle = angle_in_degrees

    def move(self, distance: float):
        angle_radians = radians(self.__angle)
        self.__x += math.cos(angle_radians) * distance
        self.__y += math.sin(angle_radians) * distance


class Bus(Car):
    COST_PER_DISTANCE_COEFFICIENT = 0.01

    def __init__(self, x: float, y: float, angle_in_degrees: float):
        super().__init__(x, y, angle_in_degrees)
        self.__passengers_count = 0
        self.__money_earned = 0

    def get_passengers_count(self):
        return self.__passengers_count

    def get_money_earned(self):
        return self.__money_earned

    def passengers_enter(self, count: int):
        if count < 0:
            raise ValueError
        self.__passengers_count += count

    def passengers_exit(self, count: int):
        if count > self.__passengers_count:
            raise ValueError
        self.__passengers_count -= count

    def move(self, distance: float):
        super().move(distance)
        self.__money_earned += distance * self.COST_PER_DISTANCE_COEFFICIENT * self.__passengers_count


bus = Bus(0, 0, 90)
assert abs(bus.get_position()[0]) < 10e-15
assert abs(bus.get_position()[1]) < 10e-15
assert bus.get_angle() == 90
assert bus.get_passengers_count() == 0
assert bus.get_money_earned() == 0

bus.move(10)
assert abs(bus.get_position()[0]) < 10e-15
assert abs(bus.get_position()[1] - 10) < 10e-15
assert bus.get_angle() == 90
assert bus.get_passengers_count() == 0
assert bus.get_money_earned() == 0

bus.passengers_enter(4)
bus.set_angle(0)
bus.move(100)
assert abs(bus.get_position()[0] - 100) < 10e-15
assert abs(bus.get_position()[1] - 10) < 10e-15
assert bus.get_angle() == 0
assert bus.get_passengers_count() == 4
assert bus.get_money_earned() == 4

bus.passengers_exit(4)
assert bus.get_passengers_count() == 0
