from kungfu_chess.model.board import Board
from kungfu_chess.model.position import Position
from kungfu_chess.rules.piece_rules import PieceRules


def _board(rows):
    return Board(rows)


def test_white_pawn_forward():
    board = _board([
        [".", ".", "."],
        [".", "wP", "."],
        [".", ".", "."],
    ])
    rules = PieceRules()
    source = Position(1, 1)
    dest = Position(0, 1)
    assert rules.is_legal_move(board, source, dest) is True


def test_black_pawn_forward():
    board = _board([
        [".", ".", "."],
        [".", "bP", "."],
        [".", ".", "."],
    ])
    rules = PieceRules()
    assert rules.is_legal_move(board, Position(1, 1), Position(2, 1)) is True


def test_pawn_diagonal_capture():
    board = _board([
        ["bR", ".", "."],
        [".", "wP", "."],
        [".", ".", "."],
    ])
    rules = PieceRules()
    assert rules.is_legal_move(board, Position(1, 1), Position(0, 0)) is True


def test_pawn_cannot_capture_forward():
    board = _board([
        [".", "bR", "."],
        [".", "wP", "."],
        [".", ".", "."],
    ])
    rules = PieceRules()
    assert rules.is_legal_move(board, Position(1, 1), Position(0, 1)) is False
def test_pawn_cannot_double_step_not_from_start():
    board = _board([
        [".", ".", "."],
        [".", ".", "."],
        [".", "wP", "."],
        [".", ".", "."],
    ])
    rules = PieceRules()

    assert rules.is_legal_move(
        board,
        Position(2, 1),
        Position(0, 1)
    ) is False