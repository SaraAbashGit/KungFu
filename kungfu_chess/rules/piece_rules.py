import json
from pathlib import Path

from kungfu_chess import constants
from kungfu_chess.model.board import Board
from kungfu_chess.model.position import Position


class RulesConfig:

    def __init__(self, rules_path=None):
        if rules_path is None:
            rules_path = Path(__file__).parent / "rules.json"
        with open(rules_path, encoding="utf-8") as file:
            self._rules = json.load(file)

    def get_rule(self, piece_type):
        return self._rules.get(piece_type)

    def is_valid_piece(self, piece_type):
        return piece_type in self._rules

    def is_jump(self, piece_type):
        return self.get_rule(piece_type)["type"] == constants.JUMP_MOVE

    def is_pawn(self, piece_type):
        return self.get_rule(piece_type)["type"] == constants.PAWN_MOVE

    def max_steps(self, piece_type):
        return self.get_rule(piece_type)["max_steps"]

    def can_move_straight(self, piece_type):
        return self.get_rule(piece_type)["straight"]

    def can_move_diagonal(self, piece_type):
        return self.get_rule(piece_type)["diagonal"]

    def jump_moves(self, piece_type):
        return self.get_rule(piece_type).get("moves", [])

    def pawn_moves(self, color):
        return self.get_rule("P")["moves"][color]

    def promotion_piece(self, piece_type):
        return self.get_rule(piece_type).get("promotion")


class PieceRules:

    def __init__(self, config: RulesConfig = None):
        self._config = config or RulesConfig()

    @property
    def config(self):
        return self._config

    def is_legal_geometry(self, board: Board, source: Position, destination: Position) -> bool:
        if source == destination:
            return False

        token = board.get_token(source)
        row_diff = destination.row - source.row
        col_diff = destination.col - source.col
        abs_row_diff = abs(row_diff)
        abs_col_diff = abs(col_diff)
        kind = token[1]

        if self._config.is_pawn(kind):
            return self._is_pawn_geometry(token, row_diff, col_diff)

        if self._config.is_jump(kind):
            return [abs_row_diff, abs_col_diff] in self._config.jump_moves(kind)

        if (
            self._config.max_steps(kind) != -1
            and (
                abs_row_diff > self._config.max_steps(kind)
                or abs_col_diff > self._config.max_steps(kind)
            )
        ):
            return False

        if abs_row_diff == abs_col_diff:
            return self._config.can_move_diagonal(kind)

        if abs_row_diff == 0 or abs_col_diff == 0:
            return self._config.can_move_straight(kind)

        return False

    def _is_pawn_geometry(self, token, row_diff, col_diff):
        color = token[0]
        return [row_diff, col_diff] in self._config.pawn_moves(color)
    def _is_pawn_double_move_valid(
        self,
        board: Board,
        source: Position,
        destination: Position,
    ):
        if board.get_kind(source) != constants.PAWN:
            return True

        row_diff = destination.row - source.row

        if abs(row_diff) != 2:
            return True

        color = board.get_color(source)

        if color == constants.WHITE and source.row != board.height - 1:
            return False

        if color == constants.BLACK and source.row != 0:
            return False

        return not board.has_piece_between(source, destination)
    def allows_destination(self, board: Board, source: Position, destination: Position) -> bool:
        token = board.get_token(source)
        kind = token[1]
        start_color = token[0]
        end_color = board.get_color(destination)

        if self._config.is_pawn(kind):
            col_diff = destination.col - source.col
            if col_diff == 0:
                return board.is_empty(destination)
            return (
                not board.is_empty(destination)
                and start_color != end_color
            )

        if board.is_empty(destination):
            return True

        return start_color != end_color

    def path_is_clear(self, board: Board, source: Position, destination: Position) -> bool:
        kind = board.get_kind(source)
        if self._config.is_jump(kind):
            return True
        return not board.has_piece_between(source, destination)

    def is_legal_move(self, board: Board, source: Position, destination: Position) -> bool:
        if board.is_empty(source):
            return False
        if not self.is_legal_geometry(board, source, destination):
            return False
        if not self._is_pawn_double_move_valid(board, source, destination):
            return False
        if not self.allows_destination(board, source, destination):
            return False
        if not self.is_legal_geometry(board, source, destination):
            return False
        return self.path_is_clear(board, source, destination)
