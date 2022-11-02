class KarmaError(RuntimeError):
    def __str__(self):
        return 'Совершён грех!'


class KillError(KarmaError):
    def __str__(self):
        return ': '.join((super().__str__()[:-1], 'убийство!'))


class DrunkError(KarmaError):
    def __str__(self):
        return ': '.join((super().__str__()[:-1], 'алкоголь!'))


class CarCrushError(KarmaError):
    def __str__(self):
        return ': '.join((super().__str__()[:-1], 'автокатастрофа!'))


class GluttonyError(KarmaError):
    def __str__(self):
        return ': '.join((super().__str__()[:-1], 'обжорство!'))


class DepressionError(KarmaError):
    def __str__(self):
        return ': '.join((super().__str__()[:-1], 'подавленность!'))


KARMA_ERRORS: list[KarmaError] = [KillError(), DrunkError(), CarCrushError(), GluttonyError(), DepressionError()]
