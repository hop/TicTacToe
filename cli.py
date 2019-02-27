from states import State


MESSAGES = {
    State.WIN: "you win!",
    State.LOSS: "you lose!",
    State.DRAW: "the game ends in a draw!",
    State.DEFAULT: "the other player conceded the game!",
    State.QUIT: "you concede!",
}


class Player(str):
    def __repr__(self):
        return f"<Player {self}>"

    def _msg(self, *args):
        # clear screen and start printing from the top
        print(f"\033[2J\033[;H", *args, sep="\n")

    def get_move(self, board):
        self._msg(board)
        while True:
            inp = input(f"player {self} > ")
            if inp == "q":
                # ^D on stdin will end the game as well
                raise EOFError
            elif inp.isdigit():
                return int(inp)

    def end(self, board, state):
        self._msg(board, f"player {self}, {MESSAGES[state]}")
