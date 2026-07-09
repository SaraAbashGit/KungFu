from movement import Movement
from board import Board
class Validator:
    def validate_board(board):
        allowed = {
            ".", "wK", "wQ", "wR", "wB", "wN", "wP",
            "bK", "bQ", "bR", "bB", "bN", "bP"}

        if len(board) == 0:
            return False

        len_row = len(board[0])    
        for i in range(len(board)):
            if len(board[i]) != len_row:
                print("ERROR ROW_WIDTH_MISMATCH")
                return False
            for j in range(len(board[i])):
                if board[i][j] not in allowed:
                    print("ERROR UNKNOWN_TOKEN")
                    return False  
        return True
    def is_valid_move(board, start, end):

        start_row, start_col = start
        end_row, end_col = end

        piece = Board.get_piece(start_row, start_col, board)

        if piece == ".":
            return False

        return Movement.is_valid_piece_move(piece,start,end)
               