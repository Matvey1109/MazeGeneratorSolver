import random

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

    def set_coin_in_maze_grid(self) -> None:
        """Sets a coin in the maze grid"""
        while True:
            c_x, c_y = random.randint(1, len(self._grid) - 2), random.randint(
                1, len(self._grid[0]) - 2
            )
            if self._grid[c_x][c_y] == TypeOfCell.EMPTY:
                self._grid[c_x][c_y] = TypeOfCell.COIN
                break

    def set_swamp_in_maze_grid(self) -> None:
        """Sets a swamp in the maze grid"""
        while True:
            s_x, s_y = random.randint(1, len(self._grid) - 2), random.randint(
                1, len(self._grid[0]) - 2
            )
            if self._grid[s_x][s_y] == TypeOfCell.EMPTY:
                self._grid[s_x][s_y] = TypeOfCell.SWAMP
                break

    def get_grid(self) -> list[list[str]]:
        """Returns the maze grid"""
        return self._grid

    def get_start_and_end_positions(
        self,
    ) -> tuple[tuple[int, int], tuple[int, int]]:
        """Returns the start and end positions of the maze"""
        start: tuple[int, int] = (0, 0)
        end: tuple[int, int] = (0, 0)

        for x_pos in range(len(self._grid)):
            for y_pos in range(len(self._grid[x_pos])):
                if self._grid[x_pos][y_pos] == TypeOfCell.POINT:
                    if start == (0, 0):
                        start = (x_pos, y_pos)
                    else:
                        end = (x_pos, y_pos)

        return (start, end)

    def update_maze_with_path(self, path: list[tuple[int, int]]) -> None:
        """Updates the maze grid with the given path"""
        for x_pos, y_pos in path:
            self._grid[x_pos][y_pos] = TypeOfCell.PATH

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
