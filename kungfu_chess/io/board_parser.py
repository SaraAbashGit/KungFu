import csv
from kungfu_chess.model.board import Board
from kungfu_chess.rules.rule_engine import RuleEngine

class BoardParser:

    def __init__(self, rule_engine: RuleEngine = None):
        self._rule_engine = rule_engine or RuleEngine()

    def parse(self, rows) -> Board | None:
        if not self._rule_engine.validate_board_tokens(rows):
            return None
        return Board(rows)
    def convert_token(self, token):

        if token == ".":
            return token

        piece = token[0]   # R,P,K...
        color = token[1]   # B,W

        if color == "B":
            color = "b"
        elif color == "W":
            color = "w"

        return color + piece
    def load_board(self,path="kungfu_chess/assets/pieces1/board.csv"):
        
        with open(path, newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)
        rows = [
                [
                    self.convert_token(cell) if cell else "."
                    for cell in row
                ]
                for row in rows
            ]
        print(rows)
        return self.parse(rows) 
    