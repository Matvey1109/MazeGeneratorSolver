from abc import ABC, abstractmethod

from maze import Maze


class Generator(ABC):
    """
    Abstract class for maze generators
    """

    def __init__(self, height: int, width: int) -> None:
        self._height: int = height
        self._width: int = width

    @abstractmethod
    def generate(self) -> Maze:
        raise NotImplementedError
