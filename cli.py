import sys
from pathlib import Path
from errors import CommandParseException

class CommandLineArgs:
    def __init__(self):
        self.args = sys.argv
        self.arg_count = 0

        self.vm_path: Path = self.get_argument("VM_PATH", Path)

        self.file: Path = self.get_argument("FILE", Path)
        if not self.file.exists():
            raise CommandParseException(
                f"The NumPoint file, {self.file}, could not be found."
            )

    def get_argument(self, name, cast: type = str):
        try:
            arg = self.args[self.arg_count]
            self.arg_count += 1
        except IndexError:
            raise CommandParseException(
                f"The commandline argument [{name}] is missing."
            )

        try:
            cast_arg = cast(arg)
        except ValueError:
            raise CommandParseException(
                f"The commandline argument [{name}] has a value of '{arg}' and connot be converted to {cast}."
            )

        return cast_arg
