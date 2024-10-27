from src.solvers.solver_factory import SolverFactory, SolverType


def test_solver_factory():
    solver = SolverFactory.get_solver(SolverType.BFS, [[]], (0, 0), (1, 1))
    assert solver is not None
    assert solver._grid == [[]]
