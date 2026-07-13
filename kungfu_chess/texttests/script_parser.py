from kungfu_chess import constants


class ScriptParser:

    def parse(self, lines):
        board_rows = []
        commands = []

        inside_board = False
        inside_commands = False

        for line in lines:
            line = line.strip()

            if line == constants.BOARD_HEADER:
                inside_board = True
                inside_commands = False
                continue

            if line == constants.COMMANDS_HEADER:
                inside_board = False
                inside_commands = True
                continue

            if inside_board:
                board_rows.append(line.split())
            elif inside_commands:
                commands.append(line)

        return board_rows, commands
