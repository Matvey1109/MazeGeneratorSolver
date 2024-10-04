class ConsolePrinter:
    @staticmethod
    def print_green(text):
        GREEN = "\033[92m"
        RESET = "\033[0m"
        return GREEN + text + RESET

    @staticmethod
    def print_red(text):
        RED = "\033[91m"
        RESET = "\033[0m"
        return RED + text + RESET
