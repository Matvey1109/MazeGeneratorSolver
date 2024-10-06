from enum import StrEnum, auto


class Position(StrEnum):
    """
    Enum class for different positions in the maze
    """

    LEFT_UP = auto()
    RIGHT_UP = auto()
    LEFT_DOWN = auto()
    RIGHT_DOWN = auto()
