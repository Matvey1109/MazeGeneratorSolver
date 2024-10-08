from solvers.solver import Solver
from type_of_cell import TypeOfCell


class DFSSolver(Solver):
    """
    Class for solver of maze based on the dfs algorithm
    """

    def __init__(
        self,
        grid: list[list[str]],
        start: tuple[int, int],
        end: tuple[int, int],
    ) -> None:
        """Initialize the DFSSolver with the specified maze, start and end"""
        super().__init__(grid, start, end)

    def solve(self) -> list[tuple[int, int]]:
        """Method to solve maze based on the dfs algorithm"""
        path: list[tuple[int, int]] = self._dfs_algorithm()
        self._refactor_path(path)

        return path

    def _dfs_algorithm(self) -> list[tuple[int, int]]:
        """Method to implement the bfs algorithm"""
        stack: list[tuple[tuple[int, int], list[tuple[int, int]]]] = [
            (self._start, [self._start])
        ]  # (current position, path)

        while stack:
            (x_pos, y_pos), path = stack.pop()  # Get the current position and path

            if (x_pos, y_pos) == self._end:
                break

            # Possible movements
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_x, next_y = x_pos + dx, y_pos + dy

                # Check bounds and conditions
                if (
                    0 <= next_x < len(self._grid)
                    and 0 <= next_y < len(self._grid[0])
                    and self._grid[next_x][next_y] != TypeOfCell.WALL
                    and (next_x, next_y) not in path
                ):

                    if self._grid[next_x][next_y] == TypeOfCell.COIN:
                        self._coin_coordinates = (next_x, next_y)
                    if self._grid[next_x][next_y] == TypeOfCell.SWAMP:
                        self._swamp_coordinates = (next_x, next_y)

                    # Add the new position and updated path to the stack
                    stack.append(((next_x, next_y), path + [(next_x, next_y)]))

        return path  # Return the path if end is reached
