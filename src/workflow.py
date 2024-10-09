from generators.generator import Generator
from maze import Maze
from solvers.solver import Solver
from stats import Stats
from ui import UI


def workflow():
    while True:
        UI.clear_screen()
        UI.hello_message()

        generator: Generator = UI.get_generator_method()
        maze: Maze = generator.generate()

        UI.print_maze(maze)

        num_points_set: int = 0
        while num_points_set < 2:
            pos: str = UI.get_position_from_user(num_points_set)
            num_points_set: int = maze.set_point(pos)

        maze.set_coin_in_maze_grid()
        maze.set_swamp_in_maze_grid()

        UI.print_maze(maze)

        start, end = maze.get_start_and_end_positions()
        grid: list[list[str]] = maze.get_grid()
        solver: Solver = UI.get_solver_method(grid, start, end)
        path: list[tuple[int, int]] = solver.solve()
        maze.update_maze_with_path(path)

        UI.print_maze(maze)

        stats: Stats = solver.get_statistics()
        UI.print_stats(stats)
        if not UI.is_playing_again():
            break
