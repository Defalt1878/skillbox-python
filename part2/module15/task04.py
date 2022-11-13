print('Задача 4. Дата')


class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, value: str) -> 'Date':
        parts = cls.__try_get_date_parts(value)
        if parts is None:
            raise ValueError('Incorrect date format!')
        return Date(*parts)

    @classmethod
    def is_date_valid(cls, value: str) -> bool:
        return cls.__try_get_date_parts(value) is not None

    @classmethod
    def __try_get_date_parts(cls, value: str) -> tuple[int, int, int] | None:
        try:
            day, month, year = map(int, value.split('-'))
            if 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999:
                return day, month, year
        except ValueError:
            pass
        return None

    def __str__(self):
        return f'День: {self.day}\tМесяц: {self.month}\tГод: {self.year}'


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
