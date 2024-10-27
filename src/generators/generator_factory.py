from enum import StrEnum, auto

from src.generators.binary_tree_generator import BinaryTreeGenerator
from src.generators.generator import IGenerator
from src.generators.wilson_generator import WilsonGenerator


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
    def get_generator(
        generator_type: GeneratorType, height: int, width: int
    ) -> IGenerator:
        match generator_type:
            case GeneratorType.BINARYTREE:
                generator: IGenerator = BinaryTreeGenerator(height, width)
            case GeneratorType.WILSON:
                generator: IGenerator = WilsonGenerator(height, width)
            case _:
                raise ValueError

        return generator
