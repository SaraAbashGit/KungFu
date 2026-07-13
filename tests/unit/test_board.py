from kungfu_chess.model.board import Board
from kungfu_chess.model.position import Position


def test_inside_board_true():
    board = Board([
        [".", "."],
        [".", "."],
    ])

    assert board.inside_bounds(Position(1, 1)) is True


def test_inside_board_false():
    board = Board([
        [".", "."],
        [".", "."],
    ])

    assert board.inside_bounds(Position(3, 0)) is False


def test_move():
    board = Board([
        ["wK", "."],
        [".", "."],
    ])

    board.move_piece(Position(0, 0), Position(1, 1))

    assert board.to_rows() == [
        [".", "."],
        [".", "wK"],
    ]
