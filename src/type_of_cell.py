from enum import StrEnum


class TypeOfCell(StrEnum):
    """
    Enum class for different types of cells in the maze
    """

    EMPTY = " "
    WALL = "#"
    COIN = "C"
    POINT = "!"
    PATH = "+"
    SWAMP = "~"
