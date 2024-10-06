from position import Position


class UI:
    # @staticmethod
    # def print_green(text):
    #     GREEN = "\033[92m"
    #     RESET = "\033[0m"
    #     return GREEN + text + RESET

    # @staticmethod
    # def print_red(text):
    #     RED = "\033[91m"
    #     RESET = "\033[0m"
    #     return RED + text + RESET

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
