from enum import Enum

print('Задача 9. Крестики-нолики')


class CellState(Enum):
    EMPTY = '_'
    CROSS = 'X'
    CIRCLE = 'O'


class Board:
    def __init__(self, size: int):
        if size < 3:
            raise ValueError('Board size cannot be less than 3')
        self.__size = size
        self.__cells = [[CellState.EMPTY] * size for _ in range(size)]

    def is_empty(self, x: int, y: int):
        return self.__cells[x][y] == CellState.EMPTY

    def set(self, x: int, y: int, value: CellState):
        if x < 0 or x >= self.__size or y < 0 or y > self.__size:
            raise ValueError('Incorrect value x or y!')
        if self.__cells[x][y] != CellState.EMPTY:
            raise ValueError('Cell is not empty!')
        self.__cells[x][y] = value
        return self.__is_win(x, y)

    def has_empty_cell(self):
        for line in self.__cells:
            for cell in line:
                if cell == CellState.EMPTY:
                    return True
        return False

    def __is_win(self, x: int, y: int):
        horizontal = self.__cells[x]
        if Board.__is_winning_line(horizontal):
            return True
        vertical = [line[y] for line in self.__cells]
        if Board.__is_winning_line(vertical):
            return True
        if x == y:
            main_diagonal = [line[i] for i, line in enumerate(self.__cells)]
            if Board.__is_winning_line(main_diagonal):
                return True
        if x + y + 1 == self.__size:
            side_diagonal = [line[self.__size - i - 1] for i, line in enumerate(self.__cells)]
            return Board.__is_winning_line(side_diagonal)
        return False

    # noinspection PyTypeChecker
    def __str__(self):
        return '\n'.join(
            [''.join(cell.value for cell in line) for line in self.__cells]
        )

    @staticmethod
    def __is_winning_line(line: list[CellState]):
        states_set = set(line)
        return states_set.pop() != CellState.EMPTY and len(states_set) == 0


board_size = 3
board = Board(board_size)

current_player = CellState.CROSS
other_player = CellState.CIRCLE

winner = None
while True:
    print('\nТекущее состояние поля:')
    print(board)
    if winner is not None:
        print(f'Победили {"крестики" if winner == CellState.CROSS else "нолики"}!')
        print('Игра окончена')
        break
    if not board.has_empty_cell():
        print('Ничья!')
        print('Игра окончена')
        break
    print(f'\nХодят {"крестики" if current_player == CellState.CROSS else "нолики"}')
    print(f'Введите через пробел два числа (столбец, строка) от 1 до {board_size}')
    coords = input('Куда хотите ходить? ').split()
    try:
        y = int(coords[0]) - 1
        x = int(coords[1]) - 1
        if not board.is_empty(x, y):
            print('В эту клетку уже установлено значение!')
            continue
        if board.set(x, y, current_player):
            winner = current_player
        (current_player, other_player) = (other_player, current_player)
    except (ValueError, IndexError):
        print('Некорректное значение! Попробуйте еще раз')
