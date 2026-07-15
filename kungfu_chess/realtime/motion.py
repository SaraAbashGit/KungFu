from kungfu_chess import constants
class Motion:
    def __init__(self, start, end, duration, motion_type=constants.NORMAL_MOVE):
        self.start = start
        self.end = end
        self.duration = duration
        self.motion_type = motion_type
        self.elapsed = 0

    def advance(self, ms):
        
        self.elapsed += ms

    def finished(self):
        return self.elapsed >= self.duration
