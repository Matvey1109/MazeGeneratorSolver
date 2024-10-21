from queue import Queue

from solvers.solver import ISolver
from type_of_cell import TypeOfCell


class BFSSolver(ISolver):
    """
    Class for solver of maze based on the bfs algorithm
    """

    def __init__(
        self,
        grid: list[list[str]],
        start: tuple[int, int],
        end: tuple[int, int],
    ) -> None:
        """Initialize the BFSSolver with the specified maze, start and end"""
        super().__init__(grid, start, end)

    def solve(self) -> list[tuple[int, int]]:
        """Method to solve maze based on the bfs algorithm"""
        path: list[tuple[int, int]] = self._bfs_algorithm()
        self._refactor_path(path)

        return path

    def _bfs_algorithm(self) -> list[tuple[int, int]]:
        """Method to implement the bfs algorithm"""
        queue: Queue = Queue()
        queue.put([self._start])  # Enqueue the start position

        while not queue.empty():
            path: list[tuple[int, int]] = queue.get()  # Dequeue the path
            x_pos, y_pos = path[-1]  # Current position is the last element of the path

            if (x_pos, y_pos) == self._end:
                break

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # Possible movements
                next_x, next_y = x_pos + dx, y_pos + dy
                if (
                    self._grid[next_x][next_y] != TypeOfCell.WALL
                    and (next_x, next_y) not in path
                ):

                    if self._grid[next_x][next_y] == TypeOfCell.COIN:
                        self._coin_coordinates = (next_x, next_y)
                    if self._grid[next_x][next_y] == TypeOfCell.SWAMP:
                        self._swamp_coordinates = (next_x, next_y)

                    new_path: list[tuple[int, int]] = list(path)
                    new_path.append((next_x, next_y))
                    queue.put(new_path)  # Enqueue the new path

        return path  # Return the path if end is reached
