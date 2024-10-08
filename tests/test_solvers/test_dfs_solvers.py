import pytest

from src.solvers.dfs_solver import DFSSolver
from src.stats import Stats


class TestDFSSolver:
    @pytest.fixture
    def dfs_solver(self) -> DFSSolver:
        """Fixture to create a DFSSolver instance for each test"""
        grid = [
            ["#", "#", "#", "#", "#"],
            ["#", " ", "C", "~", "#"],
            ["#", "!", "#", "!", "#"],
            ["#", "#", "#", "#", "#"],
        ]
        return DFSSolver(grid, (2, 1), (2, 3))

    def test_solve(self, dfs_solver: DFSSolver):
        path: list[tuple[int, int]] = dfs_solver.solve()
        assert path == [(1, 1)]

    def test_get_statistics(self, dfs_solver: DFSSolver):
        dfs_solver.solve()
        stats: Stats = dfs_solver.get_statistics()
        assert stats.length_of_path == 5
        assert stats.is_coin_found is True
        assert stats.is_swamp_found is True
