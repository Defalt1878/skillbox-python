class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[-1]

    def clear(self):
        self.__items.clear()

    def __len__(self):
        return len(self.__items)

    def __iter__(self):
        return iter(self.__items)

    def __str__(self):
        return str(self.__items)
