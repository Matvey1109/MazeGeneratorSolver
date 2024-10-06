import logging
import platform

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    # wg = WilsonGenerator(height=5, width=5)
    # maze = wg.generate()
    # num_points_set = 0
    # while num_points_set < 2:
    #     pos: str = UI.get_position_from_user(num_points_set)
    #     num_points_set: int = maze.set_point(pos)

    # for row in maze._grid:
    #     print(" ".join(row))
    logger.info(platform.python_version())


if __name__ == "__main__":
    main()
