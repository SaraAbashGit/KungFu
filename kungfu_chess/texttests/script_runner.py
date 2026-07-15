import sys

from kungfu_chess import constants
from kungfu_chess.engine.game_engine import GameEngine
from kungfu_chess.input.controller import Controller
from kungfu_chess.io.board_parser import BoardParser
from kungfu_chess.io.board_printer import BoardPrinter
from kungfu_chess.model.game_state import GameState
from kungfu_chess.realtime.real_time_arbiter import RealTimeArbiter
from kungfu_chess.rules.rule_engine import RuleEngine
from kungfu_chess.texttests.script_parser import ScriptParser


class ScriptRunner:

    def __init__(
        self,
        script_parser: ScriptParser = None,
        board_parser: BoardParser = None,
        rule_engine: RuleEngine = None,
    ):
        self._script_parser = script_parser or ScriptParser()
        self._rule_engine = rule_engine or RuleEngine()
        self._board_parser = board_parser or BoardParser(self._rule_engine)

    def run(self, input_lines=None):
        if input_lines is None:
            input_lines = sys.stdin.read().splitlines()

        board_rows, commands = self._script_parser.parse(input_lines)
        board = self._board_parser.parse(board_rows)

        if board is None:
            return

        game_state = GameState(board)
        arbiter = RealTimeArbiter()
        game_engine = GameEngine(game_state, self._rule_engine, arbiter)
        controller = Controller(board, game_engine)

        for command in commands:
            self._execute_command(command, controller, game_engine)

    def _execute_command(self, command, controller, game_engine):
        if command.startswith(constants.CLICK_COMMAND):
            parts = command.split()
            controller.click(int(parts[1]), int(parts[2]))
            return
        if command.startswith(constants.JUMP_COMMAND):
            parts = command.split()
            controller.jump(int(parts[1]), int(parts[2]))
            return
        if command.startswith(constants.WAIT_COMMAND):
            parts = command.split()
            game_engine.wait(int(parts[1]))
            return

        if command == constants.PRINT_BOARD_COMMAND:
            BoardPrinter.print(game_engine.get_board())
