from kungfu_chess.engine.game_engine import GameEngine
from kungfu_chess.input.board_mapper import BoardMapper
from kungfu_chess.model.board import Board
from kungfu_chess.model.position import Position


class Controller:

    def __init__(self, board: Board, game_engine: GameEngine, board_mapper: BoardMapper = None):
        self._board = board
        self._engine = game_engine
        self._mapper = board_mapper or BoardMapper()
        self._selected = None

    @property
    def selected(self):
        return self._selected

    def click(self, x: int, y: int):
        position = self._mapper.pixel_to_cell(x, y)

        if not self._board.inside_bounds(position):
            if self._selected is not None:
                self._selected = None
            return

        if self._selected is None:
            if not self._board.is_empty(position):
                self._selected = position
            return

        old_color = self._board.get_color(self._selected)
        new_color = self._board.get_color(position)

        if not self._board.is_empty(position) and old_color == new_color:
            self._selected = position
            return

        self._engine.request_move(self._selected, position)
        self._selected = None
    def jump(self, x: int, y: int):

        position = self._mapper.pixel_to_cell(x, y)

        if not self._board.inside_bounds(position):
            return

        self._engine.request_jump(position)