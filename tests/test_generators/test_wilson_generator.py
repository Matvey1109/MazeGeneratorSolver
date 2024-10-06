import pytest

from src.generators.wilson_generator import WilsonGenerator
from src.maze import Maze


class TestWilsonGenerator:
    @pytest.fixture
    def wilson_generator(self) -> WilsonGenerator:
        """Fixture to create a WilsonGenerator instance for each test"""
        return WilsonGenerator(5, 5)

    def test_create_zero_grid(self, wilson_generator: WilsonGenerator):
        wilson_generator._create_zero_grid()
        assert len(wilson_generator._grid) == 5
        assert len(wilson_generator._grid[0]) == 5
        assert wilson_generator._grid[0][0] == 0

    def test_get_final_grid(self, wilson_generator: WilsonGenerator):
        wilson_generator._create_zero_grid()
        final_grid: list[list[str]] = wilson_generator._get_final_grid()
        assert len(final_grid) == 11
        assert len(final_grid[0]) == 11

    def test_generate(self, wilson_generator: WilsonGenerator):
        maze: Maze = wilson_generator.generate()
        assert maze._height == 5
        assert maze._width == 5
