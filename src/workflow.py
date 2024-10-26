from src.constants import Constants
from src.generators.generator import IGenerator
from src.generators.generator_factory import GeneratorFactory
from src.maze import Maze
from src.solvers.solver import ISolver
from src.solvers.solver_factory import SolverFactory
from src.stats import Stats
from src.ui import UI


def workflow():
    """Implement workflow"""

    while True:
        UI.clear_screen()
        UI.hello_message()

        height, width = UI.get_height_and_width()
        choice: str = UI.get_generator_method()
        generator: IGenerator = GeneratorFactory.get_generator(choice, height, width)
        maze: Maze = generator.generate()

        UI.print_maze(maze)

        num_points_set: int = 0
        while num_points_set < Constants.MAX_NUMBER_OF_POINTS_IN_MAZE.value:
            pos: str = UI.get_position_from_user(num_points_set)
            num_points_set: int = maze.set_point(pos)

        maze.set_coin_in_maze_grid()
        maze.set_swamp_in_maze_grid()

        UI.print_maze(maze)

        start, end = maze.get_start_and_end_positions()
        grid: list[list[str]] = maze.get_grid()
        choice: str = UI.get_solver_method()
        solver: ISolver = SolverFactory.get_solver(choice, grid, start, end)
        path: list[tuple[int, int]] = solver.solve()
        maze.update_maze_with_path(path)

        UI.print_maze(maze)

        stats: Stats = solver.get_statistics()
        UI.print_stats(stats)
        if not UI.is_playing_again():
            break
