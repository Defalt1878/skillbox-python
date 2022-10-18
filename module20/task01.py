print('Задача 1. Ревью кода')

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def flat_map(source: list[list]):
    return [nested_e for nested in source for nested_e in nested]


def get_id_age(_students: dict):
    return [(student_id, student_info['age']) for student_id, student_info in _students.items()]


def get_interests_surnames_length(_students: dict):
    return (
        set(flat_map([student['interests'] for student in _students.values()])),
        sum(len(student['surname']) for student in _students.values())
    )


students_id_age = get_id_age(students)
print('Список пар "ID студента — возраст":', students_id_age)

interests_surnames_length = get_interests_surnames_length(students)
print('Полный список интересов всех студентов:', interests_surnames_length[0])
print('Общая длина всех фамилий студентов:', interests_surnames_length[1])
