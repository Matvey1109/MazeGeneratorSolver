from type_of_cell import TypeOfCell


class Cell:
    """
    Represents a cell in the game
    """

    def __init__(self, row: int, col: int, type: TypeOfCell):
        self.row: int = row
        self.col: int = col
        self.type: TypeOfCell = type
