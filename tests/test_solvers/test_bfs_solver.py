import pytest

from src.solvers.bfs_solver import BFSSolver
from src.stats import Stats


class TestBFSSolver:
    @pytest.fixture
    def bfs_solver(self) -> BFSSolver:
        """Fixture to create a BFSSolver instance for each test"""
        grid = [
            ["#", "#", "#", "#", "#"],
            ["#", " ", "C", "~", "#"],
            ["#", "!", "#", "!", "#"],
            ["#", "#", "#", "#", "#"],
        ]
        return BFSSolver(grid, (2, 1), (2, 3))

    def test_solve(self, bfs_solver: BFSSolver):
        path: list[tuple[int, int]] = bfs_solver.solve()
        assert path == [(1, 1)]

    def test_get_statistics(self, bfs_solver: BFSSolver):
        bfs_solver.solve()
        stats: Stats = bfs_solver.get_statistics()
        assert stats.length_of_path == 5
        assert stats.is_coin_found is True
        assert stats.is_swamp_found is True
