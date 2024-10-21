from enum import StrEnum, auto

from generators.binary_tree_generator import BinaryTreeGenerator
from generators.generator import IGenerator
from generators.wilson_generator import WilsonGenerator


class GeneratorType(StrEnum):
    """
    Enum class for generator types
    """

    BINARYTREE = auto()
    WILSON = auto()


class GeneratorFactory:
    """
    Factory class for creating generators based on the user input
    """

    @staticmethod
    def get_generator(generator_type: str, height: int, width: int) -> IGenerator:
        match generator_type:
            case GeneratorType.BINARYTREE:
                generator: IGenerator = BinaryTreeGenerator(height, width)
            case GeneratorType.WILSON:
                generator: IGenerator = WilsonGenerator(height, width)
            case _:
                raise ValueError

        return generator
