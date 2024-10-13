from generators.binary_tree_generator import BinaryTreeGenerator
from generators.generator import Generator
from generators.wilson_generator import WilsonGenerator


class GeneratorFactory:
    @staticmethod
    def get_generator(generator_type: str, height: int, width: int) -> Generator:
        if generator_type == "BINARYTREE":
            generator: Generator = BinaryTreeGenerator(height, width)
        elif generator_type == "WILSON":
            generator: Generator = WilsonGenerator(height, width)
        else:
            raise ValueError

        return generator
