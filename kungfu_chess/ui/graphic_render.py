import cv2
from kungfu_chess import constants
from .img import Img
from .sprite_manager import SpriteManager
class GraphicRender:
    def __init__(self):
        self._board_img = Img().read("kungfu_chess/assets/board.png")
        self._sprite_manager = SpriteManager()
    
    def remove_white_background(self, img):
        if img.img.shape[2] == 3:
            img.img = cv2.cvtColor(img.img, cv2.COLOR_BGR2BGRA)
        b, g, r, a = cv2.split(img.img)
        white = (b > 240) & (g > 240) & (r > 240)
        a[white] = 0
        img.img = cv2.merge((b, g, r, a))
        return img      
    
    def draw_piece_on_board(self,board): 
        board_hieght, board_width = self._board_img.img.shape[:2]
        cell_height, cell_width = board_hieght // constants.BOARD_ROWS, board_width // constants.BOARD_COLS
        grid = board.to_rows()
        for row,pieces in enumerate(grid):
            for col,piece in enumerate(pieces):
                if piece == constants.EMPTY:
                    continue
                
                piece_img = self._sprite_manager.get_sprite(piece)
                self.remove_white_background(piece_img)
                piece_img.draw_on(
                self._board_img,
                col * cell_width,
                row * cell_height
                                )
    def render(self,board):
        if board is None:
            print("Board loading failed")
            return
        self._board_img = Img().read("kungfu_chess/assets/board.png")
        self.draw_piece_on_board(board) 
        self._board_img.show()
     

