
# Board 

EMPTY = "."

BOARD_HEADER = "Board:"
COMMANDS_HEADER = "Commands:"

CELL_SIZE = 100


# Commands 

CLICK_COMMAND = "click"
WAIT_COMMAND = "wait"
PRINT_BOARD_COMMAND = "print board"
JUMP_COMMAND = "jump"


# Piece kinds

KING = "K"
PAWN = "P"
QUEEN = "Q"

# Colors 

WHITE = "w"
BLACK = "b"

VALID_COLORS = {
    WHITE,
    BLACK
}


# Rule Types 

NORMAL_MOVE = "normal"
JUMP_MOVE = "jump"
PAWN_MOVE = "pawn"

# Errors 

ERROR_UNKNOWN_TOKEN = "ERROR UNKNOWN_TOKEN"
ERROR_ROW_WIDTH_MISMATCH = "ERROR ROW_WIDTH_MISMATCH"

#Time
CELL_MOVE_TIME = 1000