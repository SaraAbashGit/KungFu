import sys
from task_1 import load_board
from task_2 import click, wait, print_board
class Game:
    def __init__(self):
        
        self.selected = None
        self.board = None
        self.commands = []
    
    def start(self):
        raw_input = sys.stdin.read()
        lines = raw_input.splitlines()
        self.board, self.commands = load_board(lines)


        if self.board is None:
            return 

        selected = None
        for command in self.commands:
            if command.startswith("click"):

                parts = command.split()

                x = int(parts[1])
                y = int(parts[2])


                self.selected = click(self.board, x, y, self.selected)

            elif command.startswith("wait"):

                parts = command.split()

                ms = int(parts[1])

                wait(ms)



            elif command == "print board":

                print_board(self.board)




