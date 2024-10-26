from enum import StrEnum, auto

from src.solvers.bfs_solver import BFSSolver
from src.solvers.dfs_solver import DFSSolver
from src.solvers.solver import ISolver


class SolverType(StrEnum):
    """
    Enum class for solver types
    """

    BFS = auto()
    DFS = auto()


class SolverFactory:
    """
    Factory class for creating solvers based on the user input
    """

    @staticmethod
    def get_solver(
        solver_type: SolverType,
        grid: list[list[str]],
        start: tuple[int, int],
        end: tuple[int, int],
    ) -> ISolver:
        match solver_type:
            case SolverType.BFS:
                solver: ISolver = BFSSolver(grid, start, end)
            case SolverType.DFS:
                solver: ISolver = DFSSolver(grid, start, end)
            case _:
                raise ValueError

        return solver
