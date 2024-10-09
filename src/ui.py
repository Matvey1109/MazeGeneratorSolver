import os

from generators.binary_tree_generator import BinaryTreeGenerator
from generators.generator import Generator
from generators.wilson_generator import WilsonGenerator
from maze import Maze
from position import Position
from solvers.bfs_solver import BFSSolver
from solvers.dfs_solver import DFSSolver
from solvers.solver import Solver
from stats import Stats
from type_of_cell import TypeOfCell


class UI:
    @staticmethod
    def get_position_from_user(num_points_set: int) -> str:  # while num_points_set < 2
        positions: list[Position] = list(Position)

        while True:
            print(
                f"Enter the position #{num_points_set + 1} (LEFT_UP, RIGHT_UP, LEFT_DOWN, RIGHT_DOWN): "
            )
            position_choice: str = input(">>> ").upper()
            if position_choice in [pos.name for pos in positions]:
                return position_choice
            else:
                print("Invalid position entered")

    @staticmethod
    def get_generator_method() -> Generator:
        """Gets generator method"""
        while True:
            height, width = UI.get_height_and_width()

            print("Choose the maze generator method (BinaryTree or Wilson): ")
            choice: str = input(">>> ").upper()
            if choice == "BINARYTREE":
                return BinaryTreeGenerator(height, width)
            elif choice == "WILSON":
                return WilsonGenerator(height, width)
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def get_solver_method(
        grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]
    ) -> Solver:
        """Gets solver method"""
        while True:
            print("Choose the maze solver method (BFS or DFS): ")
            choice: str = input(">>> ").upper()
            if choice == "BFS":
                return BFSSolver(grid, start, end)
            elif choice == "DFS":
                return DFSSolver(grid, start, end)
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def get_height_and_width() -> tuple[int, int]:
        """Gets height and width from user"""
        while True:
            try:
                height: int = int(input("Enter the height of the maze: "))
                width: int = int(input("Enter the width of the maze: "))
                if height < 3 or width < 3:
                    print("Height and width must be greater than 2")
                else:
                    return height, width
            except ValueError:
                print("Invalid input. Please enter integers only.")

    @staticmethod
    def get_green_text(text: str) -> str:
        """Return green text"""
        GREEN = "\033[92m"
        RESET = "\033[0m"
        return GREEN + text + RESET

    @staticmethod
    def get_red_text(text: str) -> str:
        """Return red text"""
        RED = "\033[91m"
        RESET = "\033[0m"
        return RED + text + RESET

    @staticmethod
    def get_cyan_text(text: str) -> str:
        """Return cyan text"""
        CYAN = "\033[96m"
        RESET = "\033[0m"
        return CYAN + text + RESET

    @staticmethod
    def get_yellow_text(text: str) -> str:
        """Return yellow text"""
        YELLOW = "\033[93m"
        RESET = "\033[0m"
        return YELLOW + text + RESET

    @staticmethod
    def print_maze(maze: Maze):
        """Displays grid of the Maze"""
        grid: list[list[str]] = maze.get_grid()

        print("Your current maze: ")
        for row in grid:
            for cell in row:
                if cell == TypeOfCell.PATH:
                    green_cell = UI.get_green_text(cell)
                    print(green_cell, end=" ")
                elif cell == TypeOfCell.SWAMP:
                    cyan_cell = UI.get_cyan_text(cell)
                    print(cyan_cell, end=" ")
                elif cell == TypeOfCell.POINT:
                    red_cell = UI.get_red_text(cell)
                    print(red_cell, end=" ")
                elif cell == TypeOfCell.COIN:
                    yellow_cell = UI.get_yellow_text(cell)
                    print(yellow_cell, end=" ")
                else:
                    print(cell, end=" ")
            print()

    @staticmethod
    def print_stats(stats: Stats):
        """Displays stats of the Maze"""
        is_coin_in_path: str = "Yes" if stats.is_coin_found else "No"
        is_swamp_in_path: str = "Yes" if stats.is_swamp_found else "No"
        print(
            f"Your stats: Length of path: {stats.length_of_path}, Is coin found: {is_coin_in_path}, Is swamp found: {is_swamp_in_path}"
        )

    @staticmethod
    def hello_message() -> None:
        """Displays a welcome message for the Maze"""
        print("Welcome to the Maze generator and solver app!")
        print("Enjoy!")
        print("*Choosen height and width will be multiply by 2*")

    @staticmethod
    def ui_menu() -> None:
        """Displays the menu options"""
        print("1. Start a new session")
        print("2. Exit")

    @staticmethod
    def is_playing_again() -> bool:
        """Asks the player to play again or exit the game"""
        while True:
            UI.ui_menu()
            choice = input(">>> ")
            if choice == "1":
                return True
            elif choice == "2":
                print("Thanks for playing!")
                return False
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def clear_screen():
        """Clears the console screen"""
        os.system("cls" if os.name == "nt" else "clear")
