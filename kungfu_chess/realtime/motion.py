class Motion:
    def __init__(self, start, end, duration):
        self.start = start
        self.end = end
        self.duration = duration
        self.elapsed = 0

    def advance(self, ms):
        
        self.elapsed += ms

    def finished(self):
        return self.elapsed >= self.duration
