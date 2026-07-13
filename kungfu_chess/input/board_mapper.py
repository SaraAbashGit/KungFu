from kungfu_chess import constants
from kungfu_chess.model.position import Position


class BoardMapper:

    @staticmethod
    def pixel_to_cell(x: int, y: int) -> Position:
        return Position(y // constants.CELL_SIZE, x // constants.CELL_SIZE)
