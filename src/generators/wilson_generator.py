import random

from src.direction import Direction
from src.generators.generator import IGenerator
from src.maze import Maze
from src.type_of_cell import TypeOfCell


class WilsonGenerator(IGenerator):
    """
    Class for maze generator based on the Wilson's algorithm
    """

    def __init__(self, height: int, width: int) -> None:
        """Initialize the WilsonGenerator with the specified height and width"""
        super().__init__(height, width)

    def generate(self) -> Maze:
        """Generate a maze using the Wilson's algorithm"""
        self._create_zero_grid()

        maze_grid: list[list[str]] = self._get_maze_grid()
        generated_maze: Maze = Maze(self._height, self._width, maze_grid)

        return generated_maze

    def _create_zero_grid(self) -> None:
        """Create a zero grid"""
        self._grid: list[list[int]] = [
            [0 for _ in range(self._width)] for _ in range(self._height)
        ]

    def _get_maze_grid(self) -> list[list[str]]:
        """Get the maze grid based on the zero grid"""
        maze_grid: list[list[str]] = [
            [TypeOfCell.WALL.value for _ in range(self._width * 2 + 1)]
            for _ in range(self._height * 2 + 1)
        ]

        total_cells: int = self._height * self._width
        cells_visited: int = 0

        # choosing random cell
        start_row: int = random.randrange(self._height)
        start_col: int = random.randrange(self._width)
        self._grid[start_row][start_col] = 1

        visited_cells: list[list[int]] = [[start_row, start_col]]
        visited_from: list[int] = [0]

        while cells_visited < total_cells:
            if self._grid[start_row][start_col] == 1:
                for idx, cell in enumerate(visited_cells):
                    v_row, v_col = cell
                    self._grid[v_row][v_col] = 1
                    row_offset = v_row * 2 + 1
                    col_offset = v_col * 2 + 1
                    maze_grid[row_offset][col_offset] = TypeOfCell.EMPTY.value

                    direction = visited_from[idx]

                    match direction:
                        case Direction.NORTH.value:
                            maze_grid[row_offset - 1][
                                col_offset
                            ] = TypeOfCell.EMPTY.value
                            maze_grid[row_offset - 2][
                                col_offset
                            ] = TypeOfCell.EMPTY.value
                        case Direction.EAST.value:
                            maze_grid[row_offset][
                                col_offset + 1
                            ] = TypeOfCell.EMPTY.value
                            maze_grid[row_offset][
                                col_offset + 2
                            ] = TypeOfCell.EMPTY.value
                        case Direction.SOUTH.value:
                            maze_grid[row_offset + 1][
                                col_offset
                            ] = TypeOfCell.EMPTY.value
                            maze_grid[row_offset + 2][
                                col_offset
                            ] = TypeOfCell.EMPTY.value
                        case Direction.WEST.value:
                            maze_grid[row_offset][
                                col_offset - 1
                            ] = TypeOfCell.EMPTY.value
                            maze_grid[row_offset][
                                col_offset - 2
                            ] = TypeOfCell.EMPTY.value

                visited_cells.clear()
                visited_from.clear()
                start_row = random.randrange(self._height)
                start_col = random.randrange(self._width)
                visited_cells.append([start_row, start_col])
                visited_from.append(0)

            else:
                if [start_row, start_col] in visited_cells:
                    visited_cells.clear()
                    visited_from.clear()

                visited_cells.append([start_row, start_col])
                can_move = [1, 1, 1, 1]

                if start_row == 0:
                    can_move[0] = 0
                if start_row == self._height - 1:
                    can_move[2] = 0
                if start_col == 0:
                    can_move[3] = 0
                if start_col == self._width - 1:
                    can_move[1] = 0

                available_moves: list[int] = [
                    index for index, value in enumerate(can_move) if value != 0
                ]

                move_direction: int = random.choice(available_moves) + 1  # n,e,s,w

                match move_direction:
                    case Direction.NORTH.value:
                        visited_from.append(Direction.NORTH.value)
                        start_row -= 1
                    case Direction.EAST.value:
                        visited_from.append(Direction.EAST.value)
                        start_col += 1
                    case Direction.SOUTH.value:
                        visited_from.append(Direction.SOUTH.value)
                        start_row += 1
                    case Direction.WEST.value:
                        visited_from.append(Direction.WEST.value)
                        start_col -= 1

            cells_visited = sum(sum(1 for val in row if val != 0) for row in self._grid)

        return maze_grid
