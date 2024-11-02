class Command:
    class Forward: ...

    class Backward: ...

    class Flip: ...

    class Print: ...

    class Inc: ...

    class Dec: ...

    class GoTo:
        to: int

        def __init__(self, to: str) -> None:
            self.to = int(to)

    class Set:
        to: int

        def __init__(self, to: str) -> None:
            self.to = int(to)

    class Jump:
        to: int

        def __init__(self, to: str) -> None:
            self.to = int(to)

    class IfEq:
        val: int

        def __init__(self, val: str) -> None:
            self.val = int(val)

    class IfNotZero: ...

    class Exit: ...


SYNTAX_MAP = {
    "fwd": Command.Forward,
    "bwd": Command.Backward,
    "flp": Command.Flip,
    "pnt": Command.Print,
    "inc": Command.Inc,
    "dec": Command.Dec,
    "gto": Command.GoTo,
    "set": Command.Set,
    "jmp": Command.Jump,
    "ieq": Command.IfEq,
    "inz": Command.IfNotZero,
    "ext": Command.Exit,
}


def cleantext(text: str) -> str:
    cleanedtext = ""
    commenton = False
    for char in text:
        if commenton:
            if char == "]":
                commenton = False
        elif char in " \t":
            if cleanedtext[-1] not in " \n":
                cleanedtext += " "
        elif char == "[":
            commenton = True
        else:
            cleanedtext += char

    return cleanedtext


def parse(text: str) -> tuple[dict, list]:
    text = cleantext(text.strip())
    commands = []
    gt_map = {}

    for line in text.split("\n"):
        elems = [x for x in line.split(" ") if x]

        if elems[0][0] == "(" and elems[0][-1] == ")":
            key = int(elems[0][1:-1])
            val = len(commands)
            gt_map[key] = val
            elems.pop(0)

        cmd = SYNTAX_MAP[elems[0]]
        elems.pop(0)
        commands.append(cmd(*elems))

    return gt_map, commands
