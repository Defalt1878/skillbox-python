from Stack import Stack


def remove_task_from_stack(tasks: Stack, task):
    temp = Stack()
    while tasks.peek() != task:
        temp.push(tasks.pop())
    tasks.pop()
    while len(temp) > 0:
        tasks.push(temp.pop())


class TaskManager:
    def __init__(self):
        self.__tasks = dict()

    def new_task(self, task: str, priority: int):
        self.remove_task(task)
        if priority not in self.__tasks:
            self.__tasks[priority] = Stack()
        self.__tasks[priority].push(task)

    def remove_task(self, task: str):
        for key, tasks in self.__tasks.items():
            if task in tasks:
                remove_task_from_stack(tasks, task)
                if len(tasks) == 0:
                    self.__tasks.pop(key)
                return

    # Замечательные костыли на которых построен весь курс!
    # Вместо того чтобы попросить сделать поиск в глубину или любую другую задачу, где действительно нужен стек
    # Мы будем учиться писать костыли! Вот они настоящие технологии программирования!

    def __str__(self):
        return '\n'.join([
            f'{priority} {"; ".join(tasks)}'
            for (priority, tasks)
            in sorted(self.__tasks.items(), key=lambda kvp: kvp[0])
        ])
