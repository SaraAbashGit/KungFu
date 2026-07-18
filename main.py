# Repository: https://github.com/SaraAbashGit/KungFu.git

from kungfu_chess.io.board_parser import BoardParser
from kungfu_chess.ui.graphic_render import GraphicRender
def main():
    # ScriptRunner().run()
    
    board = BoardParser().load_board()
    renderer = GraphicRender()
    renderer.render(board)



if __name__ == "__main__":
    main()
