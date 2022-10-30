import random

print('Задача 2. Студенты')


class Student:

    def __init__(self, full_name: str, group_number: int, *scores: float):
        self.full_name = full_name
        self.group_number = group_number
        self.scores = list(scores)

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f'{self.full_name}\t' \
               f'Группа: {self.group_number}\t' \
               f'Успеваемость: {", ".join([str(round(score, 2)) for score in self.scores])}\t' \
               f'Средний бал: {self.get_average_score():.2f}'


NAMES_LIST = ['Вова', 'Илья', 'Миша', 'Женя', 'Гена', 'Витя', 'Максим', 'Коля', 'Настя', 'Алина']


def generate_random_scores(count: int, min_score: float, max_score: float):
    return [random.uniform(min_score, max_score) for _ in range(count)]


def create_random_students(count: int):
    result = []
    for i in range(count):
        student = Student(NAMES_LIST[i % len(NAMES_LIST)], random.randint(1, 5), *generate_random_scores(5, 0, 100))
        result.append(student)

    return result


students = create_random_students(10)
students.sort(key=lambda student: student.get_average_score())
print('\n'.join([str(student) for student in students]))
