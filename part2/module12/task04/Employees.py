class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.__name = name
        self.__surname = surname
        self.__age = None
        self.set_age(age)

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def set_age(self, age: int):
        if age < 0 or age > 100:
            raise ValueError
        self.__age = age

    def __str__(self):
        return f'{self.get_name()} {self.get_surname()}, возраст: {self.get_age()}'


class Employee(Person):
    def get_salary(self):
        raise NotImplementedError

    def get_job_title(self):
        raise NotImplementedError

    def __str__(self):
        return f'{self.get_job_title()} {super().__str__()}, зарплата: {self.get_salary():.2f}'


class Manager(Employee):
    __SALARY = 13000

    def get_salary(self):
        return self.__SALARY

    def get_job_title(self):
        return 'Менеджер'


class Agent(Employee):
    __BASIC_SALARY = 5000
    __SALES_COEFFICIENT = 0.05

    def __init__(self, name: str, surname: str, age: int, sales_volume: int):
        super().__init__(name, surname, age)
        self.__sales_volume = None
        self.set_sales_volume(sales_volume)

    def get_sales_volume(self):
        return self.__sales_volume

    def set_sales_volume(self, sales_volume: int):
        if sales_volume < 0:
            raise ValueError
        self.__sales_volume = sales_volume

    def get_salary(self):
        return self.__BASIC_SALARY + self.__SALES_COEFFICIENT * self.__sales_volume

    def get_job_title(self):
        return 'Агент'


class Worker(Employee):
    __HOURS_WORKED_COEFFICIENT = 100

    def __init__(self, name: str, surname: str, age: int, hours_worked: int):
        super().__init__(name, surname, age)
        self.__hours_worked = None
        self.set_hours_worked(hours_worked)

    def get_hours_worked(self):
        return self.__hours_worked

    def set_hours_worked(self, hours_worked: int):
        if hours_worked < 0:
            raise ValueError
        self.__hours_worked = hours_worked

    def get_salary(self):
        return self.__HOURS_WORKED_COEFFICIENT * self.__hours_worked

    def get_job_title(self):
        return 'Рабочий'
