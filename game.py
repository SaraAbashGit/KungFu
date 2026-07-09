import sys
from movement import Movement
from board import Board
from input_reader import Input_reader
from validator import Validator
class Game:

    def __init__(self):
        
        self.selected = None
        self.board = None
        self.commands = []
    
    def start(self):
        raw_input = sys.stdin.read()
        lines = raw_input.splitlines()
        self.board, self.commands = Input_reader.load_board(lines)

        if not Validator.validate_board(self.board):
            return
        
        if self.board is None:
            return 

        for command in self.commands:
            if command.startswith("click"):
                parts = command.split()
                x = int(parts[1])
                y = int(parts[2])
                selected,target = Movement.click(self.board, x, y, self.selected)
                if target is not None:

                    if Validator.is_valid_move(
                        self.board,
                        selected,
                        target
                    ):
                        Board.move(
                            self.board,
                            selected,
                            target
                        )

                    self.selected = None

                else:
                    self.selected = selected
            elif command.startswith("wait"):
                parts = command.split()
                ms = int(parts[1])
                Movement.wait(ms)
            elif command == "print board":
                Board.print_board(self.board)




