print('Задача 6. Магия')


class Element:
    def name(self):
        return type(self).__name__

    def __add__(self, other):
        self_type = type(self)
        other_type = type(other)
        if self_type == other_type:
            return self
        if (self_type, other_type) in CONVERSION_TABLE:
            return CONVERSION_TABLE[(self_type, other_type)]()
        if (other_type, self_type) in CONVERSION_TABLE:
            return CONVERSION_TABLE[(other_type, self_type)]()
        return None


class Water(Element):
    pass


class Air(Element):
    pass


class Fire(Element):
    pass


class Earth(Element):
    pass


class Storm(Element):
    pass


class Steam(Element):
    pass


class Dirt(Element):
    pass


class Lightening(Element):
    pass


class Dust(Element):
    pass


class Lava(Element):
    pass


class Thunderstorm(Element):
    pass


CONVERSION_TABLE = {
    (Water, Air): Storm,
    (Water, Fire): Steam,
    (Water, Earth): Dirt,
    (Air, Fire): Lightening,
    (Air, Earth): Dust,
    (Air, Earth): Lava,
    (Lightening, Storm): Thunderstorm
}
