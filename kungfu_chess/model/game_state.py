from kungfu_chess.model.board import Board


class GameState:

    def __init__(self, board: Board, game_over: bool = False):
        self.board = board
        self.game_over = game_over
