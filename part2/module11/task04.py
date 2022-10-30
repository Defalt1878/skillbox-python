print('Задача 4. Отцы, матери и дети')


class Child:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.calm = False
        self.hungry = True


class Parent:
    def __init__(self, name: str, age: int, *children: Child):
        self.name = name
        self.age = age
        self.children = []
        for child in children:
            self.add_child(child)

    def add_child(self, child: Child):
        if self.age - child.age < 16:
            raise ValueError
        self.children.append(child)

    def calm_down_children(self):
        for child in self.children:
            child.calm = True

    def feed_children(self):
        for child in self.children:
            child.hungry = False
