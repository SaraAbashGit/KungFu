from kungfu_chess import constants
from kungfu_chess.model.position import Position


class Board:

    def __init__(self, grid):
        self._grid = grid
        self._height = len(grid)
        self._width = len(grid[0]) if grid else 0

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def inside_bounds(self, position: Position) -> bool:
        return (
            0 <= position.row < self._height
            and 0 <= position.col < self._width
        )

    def get_token(self, position: Position) -> str:
        return self._grid[position.row][position.col]

    def is_empty(self, position: Position) -> bool:
        return self.get_token(position) == constants.EMPTY

    def get_color(self, position: Position):
        token = self.get_token(position)
        if token == constants.EMPTY:
            return None
        return token[0]

    def get_kind(self, position: Position):
        token = self.get_token(position)
        if token == constants.EMPTY:
            return None
        return token[1]

    def move_piece(self, source: Position, destination: Position):
        token = self.get_token(source)
        self._grid[destination.row][destination.col] = token
        self._grid[source.row][source.col] = constants.EMPTY
        self.check_promotion(destination)
    def check_promotion(self, destination: Position):
        if self.get_kind(destination) != constants.PAWN:
            return
        if self.get_color(destination) == constants.WHITE and destination.row == 0:
            self._grid[destination.row][destination.col] =  constants.WHITE + constants.QUEEN
        elif self.get_color(destination) == constants.BLACK and destination.row == self._height-1:
            self._grid[destination.row][destination.col] = constants.BLACK+constants.QUEEN
            

    def to_rows(self):
        return self._grid

    @staticmethod
    def _step(start, end):
        if end > start:
            return 1
        if start > end:
            return -1
        return 0

    def has_piece_between(self, source: Position, destination: Position) -> bool:
        step_row = Board._step(source.row, destination.row)
        step_col = Board._step(source.col, destination.col)

        row = source.row + step_row
        col = source.col + step_col

        while (row, col) != destination.as_tuple():
            if not self.is_empty(Position(row, col)):
                return True
            row += step_row
            col += step_col

        return False
