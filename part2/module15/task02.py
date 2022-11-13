import math

print('Задача 2. Математический модуль')


class MyMath:
    pi = math.pi

    @classmethod
    def circle_len(cls, radius: float) -> float:
        return 2 * cls.pi * radius

    @classmethod
    def circle_area(cls, radius: float) -> float:
        return cls.pi * radius * radius

    @classmethod
    def cube_surface_area(cls, side_len: float) -> float:
        return 6 * side_len * side_len

    @classmethod
    def cube_volume(cls, side_len: float) -> float:
        return side_len ** 3

    @classmethod
    def sphere_surface_area(cls, radius: float) -> float:
        return 4 * cls.pi * radius * radius

    @classmethod
    def sphere_volume(cls, radius: float) -> float:
        return 4 / 3 * cls.pi * radius ** 3
