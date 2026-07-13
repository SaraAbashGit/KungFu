from kungfu_chess.model.board import Board
from kungfu_chess.rules.rule_engine import RuleEngine


class BoardParser:

    def __init__(self, rule_engine: RuleEngine = None):
        self._rule_engine = rule_engine or RuleEngine()

    def parse(self, rows) -> Board | None:
        if not self._rule_engine.validate_board_tokens(rows):
            return None
        return Board(rows)
