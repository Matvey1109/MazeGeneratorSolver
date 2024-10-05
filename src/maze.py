class Maze:
    """
    Represents a maze with cells
    """

    def __init__(self, height: int, width: int, grid: list[list[str]]):
        self.height: int = height
        self.width: int = width
        self.grid: list[list[str]] = grid  # may be need to refactor

    # def __str__(self):
    #     maze_str: str = ""
    #     for row in self.grid:
    #         for cell in row:
    #             maze_str += cell.type.value
    #         maze_str += "\n"
    #     return maze_str
