class Property:
    def __init__(self, worth):
        self._worth = worth

    def get_tax(self):
        raise NotImplementedError


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        return self._worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        return self._worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        return self._worth / 500