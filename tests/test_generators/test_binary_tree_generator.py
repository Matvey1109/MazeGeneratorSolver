import pytest

from src.generators.binary_tree_generator import BinaryTreeGenerator
from src.maze import Maze
from src.type_of_cell import TypeOfCell


class TestBinaryTreeGenerator:
    @pytest.fixture
    def binary_tree_generator(self) -> BinaryTreeGenerator:
        """Fixture to create a BinaryTreeGenerator instance for each test"""
        return BinaryTreeGenerator(5, 5)

    def test_create_random_grid(self, binary_tree_generator: BinaryTreeGenerator):
        binary_tree_generator._create_random_grid()
        assert len(binary_tree_generator._grid) == 5
        assert len(binary_tree_generator._grid[0]) == 5

    def test_preprocess_grid(self, binary_tree_generator: BinaryTreeGenerator):
        binary_tree_generator._create_random_grid()
        binary_tree_generator._preprocess_grid()
        assert binary_tree_generator._grid[0][0] == 0
        assert len(binary_tree_generator._grid) == 5
        for i in range(1, 5):
            assert binary_tree_generator._grid[i][-1] == 1

    def test_get_carved_maze(self, binary_tree_generator: BinaryTreeGenerator):
        binary_tree_generator._create_random_grid()
        binary_tree_generator._preprocess_grid()
        final_grid = binary_tree_generator._get_carved_maze()
        assert len(final_grid) == 11
        assert len(final_grid[0]) == 11

        assert final_grid[1][1] == TypeOfCell.EMPTY.value
        assert final_grid[1][2] == TypeOfCell.EMPTY.value
        assert final_grid[1][3] == TypeOfCell.EMPTY.value

        assert final_grid[3][1] == TypeOfCell.EMPTY.value
        assert final_grid[5][1] == TypeOfCell.EMPTY.value
        assert final_grid[7][1] == TypeOfCell.EMPTY.value

    def test_generate(self, binary_tree_generator: BinaryTreeGenerator):
        maze: Maze = binary_tree_generator.generate()
        assert maze._height == 5
        assert maze._width == 5
