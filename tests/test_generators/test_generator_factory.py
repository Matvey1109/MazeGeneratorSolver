from src.generators.generator_factory import GeneratorFactory, GeneratorType


def test_generator_factory():
    generator = GeneratorFactory.get_generator(GeneratorType.WILSON, 5, 5)
    assert generator is not None
    assert generator._height == 5
