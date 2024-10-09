import io

import pytest

from src.ui import UI


class TestUI:
    @pytest.mark.parametrize(
        "mock_input, user_input, expected_output",
        [
            (1, "LEFT_UP", "LEFT_UP"),
            (1, "RIGHT_UP", "RIGHT_UP"),
        ],
    )
    def test_get_position_from_user(
        self, mock_input, user_input, expected_output, monkeypatch
    ):
        monkeypatch.setattr("sys.stdin", io.StringIO(user_input))
        assert UI.get_position_from_user(mock_input) == expected_output

    def test_invalid_user_input(self, monkeypatch):
        with pytest.raises(EOFError) as exc_info:
            monkeypatch.setattr("sys.stdin", io.StringIO("error"))
            UI.get_height_and_width()

        assert exc_info.value

        with pytest.raises(EOFError) as exc_info:
            monkeypatch.setattr("sys.stdin", io.StringIO("error"))
            UI.get_generator_method()

        assert exc_info.value

        with pytest.raises(EOFError) as exc_info:
            monkeypatch.setattr("sys.stdin", io.StringIO("error"))
            UI.get_solver_method([[]], (0, 0), (0, 0))

        assert exc_info.value

    @pytest.mark.parametrize(
        "func, input, output",
        [
            (UI.get_green_text, "test", "\033[92mtest\033[0m"),
            (UI.get_red_text, "test", "\033[91mtest\033[0m"),
            (UI.get_cyan_text, "test", "\033[96mtest\033[0m"),
            (UI.get_yellow_text, "test", "\033[93mtest\033[0m"),
        ],
    )
    def test_colorful_text(self, func, input, output):
        assert func(input) == output
