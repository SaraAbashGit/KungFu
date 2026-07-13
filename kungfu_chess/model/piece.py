from kungfu_chess.model.position import Position


class Piece:

    IDLE = "idle"
    MOVING = "moving"
    CAPTURED = "captured"

    def __init__(self, piece_id: str, color: str, kind: str, cell: Position, state: str = IDLE):
        self.id = piece_id
        self.color = color
        self.kind = kind
        self.cell = cell
        self.state = state

    @staticmethod
    def from_token(token: str, piece_id: str, cell: Position):
        return Piece(piece_id, token[0], token[1], cell)

    def token(self):
        return self.color + self.kind
