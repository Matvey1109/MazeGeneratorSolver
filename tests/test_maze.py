import pytest

from src.generators.wilson_generator import WilsonGenerator
from src.maze import Maze
from src.position import Position
from src.type_of_cell import TypeOfCell


class TestMaze:
    @pytest.fixture
    def mock_maze(self) -> Maze:
        """Fixture to create a Maze instance for each test"""
        wilson_generator = WilsonGenerator(10, 10)
        maze: Maze = wilson_generator.generate()
        return maze

    @pytest.mark.parametrize(
        "mock_input, expected_output",
        [
            (Position.LEFT_UP.name, (1, 1)),
            (Position.RIGHT_UP.name, (1, -2)),
            (Position.LEFT_DOWN.name, (-2, 1)),
            (Position.RIGHT_DOWN.name, (-2, -2)),
        ],
    )
    def test_get_position_coordinates(
        self, mock_maze: Maze, mock_input, expected_output
    ):
        assert mock_maze._get_position_coordinates(mock_input) == expected_output

    def test_is_valid_position(self, mock_maze: Maze):
        assert mock_maze._is_valid_position(1, 1) is True
        assert mock_maze._is_valid_position(1, -2) is True
        assert mock_maze._is_valid_position(0, 0) is False

    def test_set_point(self, mock_maze: Maze):
        mock_maze.set_point(Position.LEFT_UP.name)
        assert mock_maze._grid[1][1] == TypeOfCell.POINT
        assert mock_maze._grid[0][0] == TypeOfCell.WALL
