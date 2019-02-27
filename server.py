#!/usr/bin/env python

from board import Board
from states import State


def play(board, player, opponent, verbose=False):
    def log(msg):
        if verbose:
            print(f"{msg}:\n\n{board}")

    while True:
        try:
            move = player.get_move(board)
            if not isinstance(move, int):
                continue
            if not 1 <= move <= 9:
                continue
            if board[move] != " ":
                continue
        except EOFError:
            player.end(board, State.QUIT)
            opponent.end(board, State.DEFAULT)
            log(f"play {player} has quit the game")
            break

        board[move] = player

        if board.is_winner(player):
            player.end(board, State.WIN)
            opponent.end(board, State.LOSS)
            log(f"player {player} has won")
            break

        if board.is_full():
            player.end(board, State.DRAW)
            opponent.end(board, State.DRAW)
            log(f"the game ended in a draw")
            break

        log(f"player {player}")

        player, opponent = opponent, player


if __name__ == "__main__":
    import argparse
    from importlib import import_module

    p = argparse.ArgumentParser(epilog="Player X goes first.")
    p.add_argument("-v", action='store_true', help="show the game's progress")
    p.add_argument("player_x", metavar="<player x>")
    p.add_argument("player_o", metavar="<player y>")
    args = p.parse_args()

    play(
        Board(),
        import_module(args.player_x).Player("x"),
        import_module(args.player_o).Player("o"),
        verbose=args.v,
    )
