import random


class Player(str):
    def __repr__(self):
        return f"<Player {self}>"

    def get_move(self, board):
        available_moves = [k for k, v in board.items() if v == " "]
        return random.choice(available_moves)

    def end(self, board, state):
        pass
