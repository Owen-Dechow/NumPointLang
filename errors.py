RED = "\033[0;31m"
GREEN = "\033[0;32m"
RESET = "\033[0m"


class CommandParseException(Exception):
    def display(self):
        print(f"{RED}ERROR:{RESET} {self}\n")


class ParserException(Exception):
    line: int

    def __init__(self, line: int, bad: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.line = line
        self.bad = bad

    def display(self, args, file_content):
        print(f"{RED}ERROR (line {self.line + 1}):{RESET} {self}")
        print(f"{args.file.absolute()}:{self.line + 1}\n")
        file_lines = file_content.splitlines()

        if self.line != 0:
            print("  ...|   " + GREEN + "..." + RESET)

        for line in range(
            self.line - 1 if self.line > 0 else self.line,
            self.line + 2 if self.line < len(file_lines) - 1 else self.line + 1,
        ):
            if line == self.line:
                line_content = file_lines[line]
                start_bad = line_content.rfind(self.bad)
                end_bad = start_bad + len(self.bad)

                first_good = line_content[:start_bad]
                bad = line_content[start_bad:end_bad]
                second_good = line_content[end_bad:]

                line_content = (
                    GREEN + first_good + RED + bad + GREEN + second_good + RESET
                )
            else:
                line_content = GREEN + file_lines[line] + RESET

            print(f"{line + 1: 5d}| {line_content}")

        if self.line != len(file_lines) - 1:
            print("  ...|   " + GREEN + "..." + RED)

        print()
