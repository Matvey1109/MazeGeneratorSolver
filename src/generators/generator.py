from abc import ABC, abstractmethod
from maze import Maze


class Generator(ABC):
    """
    Abstract class for maze generators
    """

    @abstractmethod
    def generate(self, height: int, width: int) -> Maze:
        raise NotImplementedError
