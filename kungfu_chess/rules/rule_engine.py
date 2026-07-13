from kungfu_chess import constants
from kungfu_chess.model.board import Board
from kungfu_chess.model.position import Position
from kungfu_chess.rules.piece_rules import PieceRules


class MoveValidation:

    def __init__(self, is_valid: bool, reason: str):
        self.is_valid = is_valid
        self.reason = reason


class RuleEngine:

    REASON_OK = "ok"
    REASON_OUTSIDE_BOARD = "outside_board"
    REASON_EMPTY_SOURCE = "empty_source"
    REASON_FRIENDLY_DESTINATION = "friendly_destination"
    REASON_ILLEGAL_PIECE_MOVE = "illegal_piece_move"

    def __init__(self, piece_rules: PieceRules = None):
        self._piece_rules = piece_rules or PieceRules()

    @property
    def piece_rules(self):
        return self._piece_rules

    def validate_move(self, board: Board, source: Position, destination: Position) -> MoveValidation:
        if not board.inside_bounds(source) or not board.inside_bounds(destination):
            return MoveValidation(False, self.REASON_OUTSIDE_BOARD)

        if board.is_empty(source):
            return MoveValidation(False, self.REASON_EMPTY_SOURCE)

        start_color = board.get_color(source)
        end_color = board.get_color(destination)
        if end_color is not None and start_color == end_color:
            return MoveValidation(False, self.REASON_FRIENDLY_DESTINATION)

        if not self._piece_rules.is_legal_move(board, source, destination):
            return MoveValidation(False, self.REASON_ILLEGAL_PIECE_MOVE)

        return MoveValidation(True, self.REASON_OK)

    def validate_board_tokens(self, grid) -> bool:
        if len(grid) == 0:
            return False

        row_length = len(grid[0])
        config = self._piece_rules.config

        for row in grid:
            if len(row) != row_length:
                print(constants.ERROR_ROW_WIDTH_MISMATCH)
                return False

            for token in row:
                if token == constants.EMPTY:
                    continue

                if len(token) != 2:
                    print(constants.ERROR_UNKNOWN_TOKEN)
                    return False

                if token[0] not in constants.VALID_COLORS:
                    print(constants.ERROR_UNKNOWN_TOKEN)
                    return False

                if not config.is_valid_piece(token[1]):
                    print(constants.ERROR_UNKNOWN_TOKEN)
                    return False

        return True
