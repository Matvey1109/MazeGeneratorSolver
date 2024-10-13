from solvers.solver import Solver
from solvers.bfs_solver import BFSSolver
from solvers.dfs_solver import DFSSolver


class SolverFactory:
    @staticmethod
    def get_solver(
        solver_type: str,
        grid: list[list[str]],
        start: tuple[int, int],
        end: tuple[int, int],
    ) -> Solver:
        if solver_type == "BFS":
            solver: Solver = BFSSolver(grid, start, end)
        elif solver_type == "DFS":
            solver: Solver = DFSSolver(grid, start, end)
        else:
            raise ValueError

        return solver
