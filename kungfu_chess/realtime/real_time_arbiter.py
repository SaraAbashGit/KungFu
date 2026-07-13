from kungfu_chess import constants
from kungfu_chess.realtime.motion import Motion

class RealTimeArbiter:

    def __init__(self):
        self.active_motion = []


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


    def advance_time(self, ms):

        finished = []


        for motion in self.active_motion:

            motion.advance(ms)

            if motion.finished():
                finished.append(motion)

        for motion in finished:
            self.active_motion.remove(motion)

        return finished

    def has_active_motion(self):

        return len(self.active_motion) > 0

