import sys
#from task_2 import print_board
def load_board(lines):
   
    board = []
    commands = []

    inside_board = False
    inside_commands = False

    for line in lines:
        line = line.strip()
        if line == "Board:":
            inside_board = True
            continue

        if line == "Commands:":
            inside_board = False
            inside_commands = True
            continue

        if inside_board:
            board.append(line.split())

        if inside_commands:
            commands.append(line)

    allowed = {
    ".", "wK", "wQ", "wR", "wB", "wN", "wP",
    "bK", "bQ", "bR", "bB", "bN", "bP"}

    if len(board) == 0:
       return None, None

    len_row = len(board[0])    
    for i in range(len(board)):
        if len(board[i]) != len_row:
            print("ERROR ROW_WIDTH_MISMATCH")
            return None,None
        for j in range(len(board[i])):
            if board[i][j] not in allowed:
                print("ERROR UNKNOWN_TOKEN")
                return  None,None   
    # print
    # if "print board" in commands:
    #     print_board(board)

    return board, commands