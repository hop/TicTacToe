import textwrap


WINNING_POSITIONS = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9),
    (1, 4, 7), (2, 5, 8), (3, 6, 9),
    (1, 5, 9), (3, 5, 7),
]


class Board(dict):
    def __init__(self, board=None):
        self.update(dict.fromkeys(range(1, 10), " "))
        if board:
            self.update(board)

    def __repr__(self):
        board = ''.join(self.values())
        return f"<Board |{board[:3]}|{board[3:6]}|{board[6:]}|>"

    def __str__(self):
        return textwrap.dedent(f"""\
             {self[1]} | {self[2]} | {self[3]} 
            ---+---+---
             {self[4]} | {self[5]} | {self[6]} 
            ---+---+---
             {self[7]} | {self[8]} | {self[9]} 
        """)

    def is_winner(self, player):
        for a, b, c in WINNING_POSITIONS:
            if self[a] == self[b] == self[c] == player:
                return True
        return False

    def is_full(self):
        return all(v != " " for v in self.values())
