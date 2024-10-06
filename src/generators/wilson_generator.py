import random

from generators.generator import Generator
from maze import Maze
from type_of_cell import TypeOfCell


class WilsonGenerator(Generator):
    """
    Class for maze generator based on the Wilson algorithm
    """

    def __init__(self, height: int, width: int) -> None:
        """Initialize the WilsonGenerator with the specified height and width"""
        super().__init__(height, width)

    def generate(self) -> Maze:
        """Generate a maze using the Wilson algorithm"""
        self._create_zero_grid()

        final_grid: list[list[str]] = self._get_final_grid()
        generated_maze: Maze = Maze(self._height, self._width, final_grid)

        return generated_maze

    def _create_zero_grid(self) -> None:
        """Create a zero grid"""
        grid: list[list[int]] = [
            [0 for _ in range(self._width)] for _ in range(self._height)
        ]

        self._grid: list[list[int]] = grid

    def _get_final_grid(self) -> list[list[str]]:
        """Get the final grid based on the zero grid"""
        final_grid: list[list[str]] = [
            [TypeOfCell.WALL.value for _ in range(self._width * 2 + 1)]
            for _ in range(self._height * 2 + 1)
        ]

        c: int = self._height * self._width  # number of cells to be visited

        # choose random cell
        i: int = random.randrange(self._height)
        j: int = random.randrange(self._width)
        self._grid[i][j] = 1

        visited: list[list[int]] = [[i, j]]
        visited_from: list[int] = [0]

        while sum(sum(1 for val in row if val != 0) for row in self._grid) < c:
            if self._grid[i][j] == 1:
                for i in range(len(visited)):
                    ve = visited[i]
                    vi = ve[0]
                    vj = ve[1]
                    self._grid[vi][vj] = 1
                    w = vi * 2 + 1
                    k = vj * 2 + 1
                    final_grid[w][k] = " "

                    vf = visited_from[i]

                    if vf == 1:
                        final_grid[w - 1][k] = " "
                        final_grid[w - 2][k] = " "
                    elif vf == 2:
                        final_grid[w][k + 1] = " "
                        final_grid[w][k + 2] = " "
                    elif vf == 3:
                        final_grid[w + 1][k] = " "
                        final_grid[w + 2][k] = " "
                    elif vf == 4:
                        final_grid[w][k - 1] = " "
                        final_grid[w][k - 2] = " "

                visited.clear()
                visited_from.clear()
                i = random.randrange(self._height)
                j = random.randrange(self._width)
                visited.append([i, j])
                visited_from.append(0)

            else:
                if [i, j] in visited:
                    visited.clear()
                    visited_from.clear()

                visited.append([i, j])
                can_go = [1, 1, 1, 1]

                if i == 0:
                    can_go[0] = 0
                if i == self._height - 1:
                    can_go[2] = 0
                if j == 0:
                    can_go[3] = 0
                if j == self._width - 1:
                    can_go[1] = 0

                nonzero_indices: list[int] = [
                    index for index, value in enumerate(can_go) if value != 0
                ]

                neighbour_idx: int = random.choice(nonzero_indices)  # n,e,s,w

                if neighbour_idx == 0:
                    # going there from s
                    visited_from.append(1)
                    i -= 1

                if neighbour_idx == 1:
                    visited_from.append(2)
                    j += 1

                if neighbour_idx == 2:
                    visited_from.append(3)
                    i += 1

                if neighbour_idx == 3:
                    visited_from.append(4)
                    j -= 1

        return final_grid
