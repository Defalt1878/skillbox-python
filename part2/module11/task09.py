from enum import Enum

print('Задача 9. Крестики-нолики')


class CellState(Enum):
    EMPTY = '_'
    CROSS = 'X'
    CIRCLE = 'O'


class Board:
    def __init__(self):
        self.cells = [[CellState.EMPTY] * 3 for _ in range(3)]

    def is_empty(self, x: int, y: int):
        return self.cells[x][y] == CellState.EMPTY

    def set(self, x: int, y: int, value: CellState):
        if self.cells[x][y] != CellState.EMPTY:
            raise ValueError
        self.cells[x][y] = value

    def has_empty(self):
        for line in self.cells:
            for cell in line:
                if cell == CellState.EMPTY:
                    return True
        return False

    def get_winner(self):
        winners = [
            self.get_horizontal_winner(),
            self.get_vertical_winner(),
            self.get_diagonal_winner()
        ]
        winners = [winner for winner in winners if winner is not None]
        if len(winners) == 0:
            return None
        return winners.pop()

    def get_horizontal_winner(self):
        for line in self.cells:
            if Board.is_win(line):
                return line[0]
        return None

    def get_vertical_winner(self):
        for x in range(3):
            line = [line[x] for line in self.cells]
            if Board.is_win(line):
                return line[0]
        return None

    def get_diagonal_winner(self):
        main_diagonal = [line[y] for y, line in enumerate(self.cells)]
        side_diagonal = [line[2 - y] for y, line in enumerate(self.cells)]
        if Board.is_win(main_diagonal):
            return main_diagonal[0]
        if Board.is_win(side_diagonal):
            return side_diagonal[0]
        return None

    # noinspection PyTypeChecker
    def __str__(self):
        return '\n'.join(
            [''.join(cell.value for cell in line) for line in self.cells]
        )

    @staticmethod
    def is_win(line: list[CellState]):
        states_set = set(line)
        return states_set.pop() != CellState.EMPTY and len(states_set) == 0


board = Board()

current_player = CellState.CROSS
other_player = CellState.CIRCLE

while True:
    print('\nТекущее состояние поля:')
    print(board)
    winner = board.get_winner()
    if winner is not None:
        print(f'Победили {"крестики" if winner == CellState.CROSS else "нолики"}!')
        print('Игра окончена')
        break
    if not board.has_empty():
        print('Ничья!')
        print('Игра окончена')
        break
    print(f'\nХодят {"крестики" if current_player == CellState.CROSS else "нолики"}')
    print('Введите через пробел два числа (столбец, строка) от 1 до 3')
    coords = input('Куда хотите ходить? ').split()
    y = int(coords[0]) - 1
    x = int(coords[1]) - 1
    if not board.is_empty(x, y):
        print('В эту клетку уже установлено значение!')
        continue
    board.set(x, y, current_player)
    (current_player, other_player) = (other_player, current_player)
