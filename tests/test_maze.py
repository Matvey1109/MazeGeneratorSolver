import pytest

from src.generators.wilson_generator import WilsonGenerator
from src.maze import Maze
from src.position import Position
from src.solvers.bfs_solver import BFSSolver
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

    def test_set_coin_in_maze_grid(self, mock_maze: Maze):
        mock_maze.set_coin_in_maze_grid()
        number_of_coins: int = 0

        for row in mock_maze._grid:
            for cell in row:
                if cell == TypeOfCell.COIN:
                    number_of_coins += 1

        assert number_of_coins == 1

    def test_set_swamp_in_maze_grid(self, mock_maze: Maze):
        mock_maze.set_swamp_in_maze_grid()
        number_of_swamps: int = 0

        for row in mock_maze._grid:
            for cell in row:
                if cell == TypeOfCell.SWAMP:
                    number_of_swamps += 1

        assert number_of_swamps == 1

    def test_correct_view_of_path(self):
        grid = [
            ["#", "#", "#", "#", "#"],
            ["#", " ", "C", "~", "#"],
            ["#", "!", "#", "!", "#"],
            ["#", "#", "#", "#", "#"],
        ]
        maze = Maze(5, 5, grid)
        bfs_solver = BFSSolver(grid, (2, 1), (2, 3))

        path: list[tuple[int, int]] = bfs_solver.solve()
        maze.update_maze_with_path(path)

        assert maze._grid == [
            ["#", "#", "#", "#", "#"],
            ["#", "+", "C", "~", "#"],
            ["#", "!", "#", "!", "#"],
            ["#", "#", "#", "#", "#"],
        ]
