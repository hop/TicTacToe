from enum import Enum, auto


class State(Enum):
    WIN = auto()
    LOSS = auto()
    DRAW = auto()
    DEFAULT = auto()
    QUIT = auto()
