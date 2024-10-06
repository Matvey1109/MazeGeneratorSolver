from position import Position
from type_of_cell import TypeOfCell


class Maze:
    """
    Represents a maze with cells
    """

    def __init__(self, height: int, width: int, grid: list[list[str]]) -> None:
        self._height: int = height
        self._width: int = width
        self._grid: list[list[str]] = grid  # may be need to refactor
        self._num_points_set = 0

    def set_point(self, position_choice: str) -> int:
        """Sets a point in the maze at the specified position"""
        row, col = self._get_position_coordinates(position_choice.upper())

        if self._is_valid_position(row, col):
            self._grid[row][col] = TypeOfCell.POINT
            self._num_points_set += 1
        else:
            print("Invalid position or position already set")

        return self._num_points_set

    def _is_valid_position(self, row: int, col: int) -> bool:
        """Checks if the position in the maze is valid (empty)"""
        return self._grid[row][col] == TypeOfCell.EMPTY

    def _get_position_coordinates(self, position: str) -> tuple[int, int]:
        """Returns position coordinates based on the given position choice"""
        positions = {
            Position.LEFT_UP.name: (1, 1),
            Position.RIGHT_UP.name: (1, -2),
            Position.LEFT_DOWN.name: (-2, 1),
            Position.RIGHT_DOWN.name: (-2, -2),
        }

        return positions.get(position, (1, 1))


# def __str__(self):
#     maze_str: str = ""
#     for row in self.grid:
#         for cell in row:
#             maze_str += cell.type.value
#         maze_str += "\n"
#     return maze_str
