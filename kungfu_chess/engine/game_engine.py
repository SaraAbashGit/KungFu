from kungfu_chess import constants
from kungfu_chess.model.game_state import GameState
from kungfu_chess.model.position import Position
from kungfu_chess.realtime.real_time_arbiter import RealTimeArbiter
from kungfu_chess.rules.rule_engine import RuleEngine


class MoveResult:

    def __init__(self, is_accepted: bool, reason: str):
        self.is_accepted = is_accepted
        self.reason = reason


class GameEngine:

    REASON_OK = "ok"
    REASON_GAME_OVER = "game_over"
    REASON_MOTION_IN_PROGRESS = "motion_in_progress"

    def __init__(self, game_state: GameState, rule_engine: RuleEngine, arbiter: RealTimeArbiter):
        self._state = game_state
        self._rule_engine = rule_engine
        self._arbiter = arbiter

    @property
    def state(self):
        return self._state

    def get_board(self):
        return self._state.board

    def request_move(self, source: Position, destination: Position) -> MoveResult:
        if self._state.game_over:
            return MoveResult(False, self.REASON_GAME_OVER)

        if self._arbiter.has_active_move():
            return MoveResult(False, self.REASON_MOTION_IN_PROGRESS)

        validation = self._rule_engine.validate_move(
            self._state.board,
            source,
            destination,
        )

        if not validation.is_valid:
            return MoveResult(False, validation.reason)

        self._arbiter.start_motion(source.as_tuple(), destination.as_tuple())
        return MoveResult(True, self.REASON_OK)
    def request_jump(self, position: Position) -> MoveResult:

        if self._state.game_over:
            return MoveResult(False, self.REASON_GAME_OVER)

        if self._arbiter.has_motion_at(position.as_tuple()):
            return MoveResult(False, self.REASON_MOTION_IN_PROGRESS)

        piece = self._state.board.get_token(position)

        if piece == constants.EMPTY:
            return MoveResult(False, "empty_cell")

        self._arbiter.start_jump(position.as_tuple())

        return MoveResult(True, self.REASON_OK)
    def wait(self, milliseconds: int):

        finished = self._arbiter.advance_time(milliseconds)

        for motion in finished:

            if motion.motion_type == constants.JUMP_MOVE:
                continue

            jump = self._arbiter.get_jump_at(motion.end)
            

            if jump is not None:
                self._state.board.remove_piece(
                    Position.from_tuple(motion.start)
                )
                continue
            destination = Position.from_tuple(motion.end)

            captured_token = self._state.board.get_token(destination)

            self._state.board.move_piece(
                Position.from_tuple(motion.start),
                destination,
            )

            if self._is_king(captured_token):
                self._state.game_over = True
        self._arbiter.finished_jumps.clear()  

    @staticmethod
    def _is_king(token: str) -> bool:
        return len(token) == 2 and token[1] == constants.KING
