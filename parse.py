from errors import ParserException

class Command:
    def __init__(self, _: int) -> None: ...


class IntCommand:
    val: int

    def __init__(self, val: str, line: int) -> None:
        try:
            self.val = int(val)
        except ValueError:
            raise ParserException(
                line, val, f"'{val}' could not be converted to {int}."
            )


class CMDS:
    class Forward(Command): ...

    class Backward(Command): ...

    class Flip(Command): ...

    class Print(Command): ...

    class Inc(Command): ...

    class Dec(Command): ...

    class GoTo(IntCommand): ...

    class Set(IntCommand): ...

    class Jump(IntCommand): ...

    class IfEq(IntCommand): ...

    class IfNotZero(Command): ...

    class Exit(Command): ...


SYNTAX_MAP = {
    "fwd": CMDS.Forward,
    "bwd": CMDS.Backward,
    "flp": CMDS.Flip,
    "pnt": CMDS.Print,
    "inc": CMDS.Inc,
    "dec": CMDS.Dec,
    "gto": CMDS.GoTo,
    "set": CMDS.Set,
    "jmp": CMDS.Jump,
    "ieq": CMDS.IfEq,
    "inz": CMDS.IfNotZero,
    "ext": CMDS.Exit,
}


def cleantext(text: str) -> tuple[str, dict[int, int]]:
    line_map = {}
    user_line = 0
    program_line = 0
    cleaned_text = ""
    comment_on = False
    for char in text:
        if comment_on:
            if char == "]":
                comment_on = False
            elif char == "\n":
                user_line += 1
        elif char in " \t":
            if cleaned_text and cleaned_text[-1] not in " \n":
                cleaned_text += " "
        elif char == "[":
            comment_on = True
        elif char == "\n":
            if cleaned_text and cleaned_text[-1] != "\n":
                cleaned_text += char
                line_map[program_line] = user_line
                program_line += 1
            user_line += 1
        else:
            cleaned_text += char

    line_map[program_line] = user_line
    return cleaned_text.strip(), line_map


def parse(text: str) -> tuple[dict, list]:
    text, line_map = cleantext(text.strip())
    commands = []
    gt_map = {}

    for line_num, line in enumerate(text.split("\n")):
        elems = [x for x in line.split(" ") if x]

        if elems[0][0] == "(" and elems[0][-1] == ")":
            val = len(commands)
            str_key = elems[0][1:-1]
            try:
                key = int(str_key)
            except ValueError:
                raise ParserException(
                    line_map[line_num],
                    str_key,
                    f"'{str_key}' could not be converted to {int}."
                )
            gt_map[key] = val
            elems.pop(0)

        if elems[0] in SYNTAX_MAP:
            cmd = SYNTAX_MAP[elems[0]]
            cmd_key = elems.pop(0)
        else:
            raise ParserException(
                line_map[line_num], elems[0], f"'{elems[0]}' is not a known command."
            )

        if issubclass(cmd, IntCommand):
            if len(elems) == 0:
                raise ParserException(
                    line_map[line_num],
                    "",
                    f"'{cmd_key}' must be followed by an integer argument.",
                )
            elif len(elems) > 1:
                raise ParserException(
                    line_map[line_num],
                    elems[1],
                    "Cannot have multiple commands on one line.",
                )
        else:
            if len(elems) > 0:
                extra: str = elems[0]
                raise ParserException(
                    line_map[line_num],
                    extra,
                    f"'{cmd_key}' does not take any arguments."
                    if extra.isnumeric()
                    else "Cannot have multiple commands on one line.",
                )

        commands.append(cmd(*elems, line_map[line_num]))

    return gt_map, commands
