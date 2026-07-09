class Board:

    def inside_board(row,col,board):
        return 0 <= row < len(board) and 0 <= col < len(board[0])
    
    def get_piece(row,col,board):
        return board[row][col]
    
    def move(board,start,end,):
        start_row,start_col = start
        end_row,end_col = end

        piece = board[start_row][start_col]
        board[end_row][end_col] = piece
        board[start_row][start_col] = "."
    
    def print_board(board):
        for row in board:
            print(" ".join(row))
