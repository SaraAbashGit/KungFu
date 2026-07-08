import sys
def pixel(x,y):
    row = y//100
    col = x//100
    return row,col
def inside_board(row,col,board):
    return 0 <= row < len(board) and 0 <= col < len(board[0])
def get_piece(row,col,board):
    return board[row][col]
def click(board,x,y,selected):

    row,col = pixel(x,y)

    if inside_board(row,col,board) == False:
        return selected
        
    piece = get_piece(row,col,board)

    if selected is None:
       if piece != ".":
           selected = (row,col)
    else:
        old_piece = get_piece(selected[0],selected[1],board)

        if piece!="." and old_piece[0] == piece[0]:
            selected = (row,col)
        else:
            move(board,selected,(row,col))
            selected = None
    
    return selected
def move(board,start,end,):
    start_row,start_col = start
    end_row,end_col = end

    piece = board[start_row][start_col]
    board[end_row][end_col] = piece
    board[start_row][start_col] = "."

def wait(ms):
    pass

def print_board(board):
    for row in board:
        print(" ".join(row))




