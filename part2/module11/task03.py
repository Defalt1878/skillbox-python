import math

print('Задача 3. Круг')


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.radius = r

    def get_square(self):
        return math.pi * math.pi * self.radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def increase(self, k: int):
        self.radius *= k

    def is_intersect(self, other):
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        centers_distance = math.sqrt(dx * dx + dy * dy)
        return centers_distance <= self.radius + other.radius
