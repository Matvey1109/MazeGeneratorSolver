from abc import ABC, abstractmethod

from stats import Stats


class Solver(ABC):
    """
    Abstract class for solver of maze
    """

    def __init__(
        self,
        grid: list[list[str]],
        start: tuple[int, int],
        end: tuple[int, int],
    ) -> None:
        self._grid: list[list[str]] = grid
        self._start: tuple[int, int] = start
        self._end: tuple[int, int] = end
        self._length_of_path: int = 0
        self._is_coin_found: bool = False
        self._is_swamp_found: bool = False
        self._coin_coordinates: tuple[int, int] = (0, 0)
        self._swamp_coordinates: tuple[int, int] = (0, 0)

    @abstractmethod
    def solve(self) -> list[tuple[int, int]]:
        """Abstract method to solve maze"""
        raise NotImplementedError

    def get_statistics(self) -> Stats:
        """Method to get statistics of solving"""
        stats: Stats = Stats(
            self._length_of_path, self._is_coin_found, self._is_swamp_found
        )
        return stats

    def _refactor_path(self, path: list[tuple[int, int]]) -> None:
        """Method to refactor the path"""
        self._length_of_path = len(path)

        path.pop(0)
        path.pop()

        if self._coin_coordinates in path:
            self._is_coin_found = True
            path.remove(self._coin_coordinates)
        if self._swamp_coordinates in path:
            self._is_swamp_found = True
            path.remove(self._swamp_coordinates)
