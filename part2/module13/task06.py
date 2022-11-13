print('Задача 6. Односвязный список')


class LinkedListNode:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    @property
    def value(self):
        return self.__value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value: 'LinkedListNode'):
        self.__next = value


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def append(self, value):
        if self.__head is None:
            added = self.__head = LinkedListNode(value)
        else:
            added = self.__tail.next = LinkedListNode(value)
        self.__tail = added
        self.__len += 1

    def get(self, index):
        if index < 0:
            index = self.__len + index
        if index < 0 or index >= self.__len:
            raise IndexError

        current = self.__head
        for _ in range(index):
            current = current.next

        return current.value

    def remove(self, index):
        if index < 0:
            index = self.__len + index
        if index < 0 or index >= self.__len:
            raise IndexError

        if index == 0:
            self.__head = self.__head.next
            if self.__head is None:
                self.__tail = None
        else:
            current = self.__head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
            if current.next is None:
                self.__tail = current

        self.__len -= 1

    def __len__(self):
        return self.__len

    def __iter__(self):
        current = self.__head
        while current is not None:
            yield current.value
            current = current.next

    def __str__(self):
        return f'[{", ".join((str(e) for e in self))}]'


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
