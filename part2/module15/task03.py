import math
from abc import ABC, abstractmethod

print('Задача 3. Моделирование')


class Figure2D(ABC):
    @abstractmethod
    def get_perimeter(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_square(self) -> float:
        raise NotImplementedError


class Square(Figure2D):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, value: float):
        if value < 0:
            raise ValueError('Width should be positive.')
        self.__width = value

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, value: float):
        if value < 0:
            raise ValueError('Height should be positive.')
        self.__height = value

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def get_square(self) -> float:
        return self.width * self.height


class IsoscelesTriangle(Figure2D):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    @property
    def base(self) -> float:
        return self.__base

    @base.setter
    def base(self, value: float):
        if value < 0:
            raise ValueError('Base should be positive.')
        self.__base = value

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, value: float):
        if value < 0:
            raise ValueError('Height should be positive.')
        self.__height = value

    def get_perimeter(self) -> float:
        return self.base + math.sqrt(self.base * self.base + 4 * self.height * self.height)

    def get_square(self) -> float:
        return self.base * self.height / 2


class Figure3D(ABC):
    def __init__(self, *sides: Figure2D):
        self._sides = list(sides)

    def get_surface_square(self) -> float:
        return sum(side.get_square() for side in self._sides)


class Cube(Figure3D):
    def __init__(self, *sides: Square):
        if len(sides) != 6:
            raise ValueError
        super().__init__(*sides)


class Pyramid(Figure3D):
    def __init__(self, *sides: IsoscelesTriangle, base: Square):
        if len(sides) != 4:
            raise ValueError
        super().__init__(*sides, base)
