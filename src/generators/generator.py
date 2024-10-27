from abc import ABC, abstractmethod

from src.maze import Maze


class IGenerator(ABC):
    """
    Abstract class for maze generators
    """

    def __init__(self, height: int, width: int) -> None:
        self._height: int = height
        self._width: int = width
        self._grid: list[list[int]] = []

    @abstractmethod
    def generate(self) -> Maze:
        """Abstract method to generate maze"""
        raise NotImplementedError
