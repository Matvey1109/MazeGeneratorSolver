from abc import ABC, abstractmethod


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

    @abstractmethod
    def solve(self) -> list[tuple[int, int]]:
        """Abstract method to solve maze"""
        raise NotImplementedError

    def get_statistics(self) -> tuple[int, bool, bool]:
        """Method to get statistics of solving"""
        return (self._length_of_path, self._is_coin_found, self._is_swamp_found)
