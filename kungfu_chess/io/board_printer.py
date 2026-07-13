from kungfu_chess.model.board import Board


class BoardPrinter:

    @staticmethod
    def print(board: Board):
        for row in board.to_rows():
            print(" ".join(row))
