from board import Board
from rules import Rules
class Movement:

    rules = Rules()
    def pixel(x,y):
        row = y//100
        col = x//100
        return row,col
    def is_valid_piece_move(piece, start, end):

        if start == end:
            return False

        start_row, start_col = start
        end_row, end_col = end

        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        kind = piece[1]

        rule = Movement.rules.get_rule(kind)

        if rule["type"] == "jump":
            return [row_diff, col_diff] in rule["moves"]


        if (
            rule["max_steps"] != -1 and
            (
                row_diff > rule["max_steps"] or
                col_diff > rule["max_steps"]
            )
        ):
            return False


        if row_diff == col_diff:

            return rule["diagonal"]


        if row_diff == 0 or col_diff == 0:

            return rule["straight"]


        return False

        
    def click(board,x,y,selected):

        row,col = Movement.pixel(x,y)

        if Board.inside_board(row,col,board) == False:
            return selected , None
            
        piece = Board.get_piece(row,col,board)

        if selected is None:
            if piece != ".":
                selected = (row,col)
        else:
            old_piece = Board.get_piece(selected[0],selected[1],board)

            if piece!="." and old_piece[0] == piece[0]:
                selected = (row,col)
            else:
                return selected,(row,col)
        
        return selected,None
    def wait(ms):
        pass
# if __name__ == "__main__":
#      print(
#         Movement.is_valid_piece_move(
#             "wK",
#             (0, 0),
#             (1, 1)
#         )
#     )
    
