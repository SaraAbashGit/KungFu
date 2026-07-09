class Input_reader:
    def load_board(lines):
   
        board = []
        commands = []

        inside_board = False
        inside_commands = False

        for line in lines:
            line = line.strip()
            if line == "Board:":
                inside_board = True
                continue

            if line == "Commands:":
                inside_board = False
                inside_commands = True
                continue

            if inside_board:
                board.append(line.split())

            if inside_commands:
                commands.append(line)

        return board, commands