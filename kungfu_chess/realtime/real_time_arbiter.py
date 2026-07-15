from kungfu_chess import constants
from kungfu_chess.realtime.motion import Motion

class RealTimeArbiter:

    def __init__(self):
        self.active_motion = []
        self.finished_jumps = []


    def start_motion(self, start, end):
        distance = max(
            abs(end[0] - start[0]),
            abs(end[1] - start[1])
        )

        duration = distance * constants.CELL_MOVE_TIME

        motion = Motion(
            start,
            end,
            duration
        )
        self.active_motion.append(motion)

    def start_jump(self, position):
        motion = Motion(
            position,
            position,
            constants.CELL_MOVE_TIME,
            constants.JUMP_MOVE
        )
        self.active_motion.append(motion)
    def advance_time(self, ms):

        finished = []
        for motion in self.active_motion:

            motion.advance(ms)

            if motion.finished():
                finished.append(motion)

        for motion in finished:
            self.active_motion.remove(motion)
            if motion.motion_type == constants.JUMP_MOVE:
                self.finished_jumps.append(motion)
        return finished

    def has_active_motion(self):

        return len(self.active_motion) > 0
    def has_active_move(self):

        for motion in self.active_motion:
            if motion.motion_type == constants.NORMAL_MOVE:
                return True

        return False
    

    def get_jump_at(self, position):

        motions = self.active_motion + self.finished_jumps

        for motion in motions:
            if (
                motion.motion_type == constants.JUMP_MOVE
                and motion.end == position
            ):
                return motion

        return None
    def has_motion_at(self, position):

        for motion in self.active_motion:

            if (
                motion.motion_type == constants.NORMAL_MOVE
                and motion.start == position
            ):
                return True

        return False
    

    