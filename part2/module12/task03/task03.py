print('Задача 3. Свой словарь')


class MyDict(dict):
    def get(self, key):
        return super().get(key, 0)


my_dict = MyDict()
my_dict['x'] = 'y'
my_dict['y'] = 'z'

assert my_dict.get('x') == 'y'
assert my_dict.get('y') == 'z'
assert my_dict.get('z') == 0
