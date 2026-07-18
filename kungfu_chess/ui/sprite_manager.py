from kungfu_chess.ui.img import Img
from kungfu_chess import constants
class SpriteManager:
    def __init__(self):
       pass
    def convert_token(self, token):

            color = token[0]   # b/w
            piece = token[1]   # R/P/K...

            if color == "b":
                color = "B"
            elif color == "w":
                color = "W"

            return piece + color

    def get_sprite(self,piece_token:str,state:str="idle",frame:int=1):
        sprite_token = self.convert_token(piece_token)

        print("received:", piece_token)
        print("converted:", sprite_token)

        image_path = (
            f"kungfu_chess/assets/pieces1/"
            f"{sprite_token}/states/"
            f"{state}/sprites/"
            f"{frame}.png"
        )
        sprite = Img().read(
            image_path,
            size=(constants.CELL_SIZE, constants.CELL_SIZE)
        )
        return sprite
    