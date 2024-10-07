import pytest

from src.solvers.bfs_solver import BFSSolver


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
        length_of_path, is_coin_found, is_swamp_found = bfs_solver.get_statistics()
        assert length_of_path == 5
        assert is_coin_found is True
        assert is_swamp_found is True
