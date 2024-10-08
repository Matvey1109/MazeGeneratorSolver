import logging
import platform

# from generators.wilson_generator import WilsonGenerator
# from ui import UI
# from solvers.dfs_solver import DFSSolver

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    # wg = WilsonGenerator(height=5, width=5)
    # maze = wg.generate()
    # for el in maze._grid:
    #     print(" ".join(el))
    # num_points_set = 0
    # while num_points_set < 2:
    #     pos: str = UI.get_position_from_user(num_points_set)
    #     num_points_set: int = maze.set_point(pos)

    # maze.set_coin_in_maze_grid()
    # maze.set_swamp_in_maze_grid()
    # grid = maze.get_grid()
    # start, end = maze.get_start_and_end_positions()

    # for el in maze._grid:
    #     print(" ".join(el))

    # dfs_solver = DFSSolver(grid, start, end)
    # path = dfs_solver.solve()
    # maze.update_maze_with_path(path)

    # for row in maze._grid:
    #     print(" ".join(row))

    # s = dfs_solver.get_statistics()
    # print(s)

    logger.info(platform.python_version())


if __name__ == "__main__":
    main()
