from parse import Command

PAPER_LENGTH: int = 30_000


def process_command_list(paper: list[int], commands: list, goto_map: dict[int, int]):
    LAST_PAPER_IDX = PAPER_LENGTH - 1
    NUM_COMMANDS = len(commands)
    ptr: int = 0
    cmd_ptr: int = 0

    while cmd_ptr < NUM_COMMANDS:
        command = commands[cmd_ptr]

        match type(command):
            case Command.Forward:
                ptr = ptr + 1 if ptr < LAST_PAPER_IDX else 0
            case Command.Backward:
                ptr = ptr - 1 if ptr > 0 else LAST_PAPER_IDX
            case Command.Jump:
                ptr = command.to % PAPER_LENGTH
            case Command.Flip:
                paper[ptr] = int(not paper[ptr])
            case Command.Print:
                print(
                    bytes(paper[ptr : (paper + [0])[ptr:].index(0)]).decode("UTF-8"),
                    end="\n",
                )
            case Command.Inc:
                paper[ptr] += 1
            case Command.Dec:
                paper[ptr] -= 1
            case Command.Set:
                paper[ptr] = command.to
            case Command.GoTo:
                cmd_ptr = goto_map[command.to] - 1
            case Command.IfEq:
                if paper[ptr] != command.val:
                    cmd_ptr += 1
            case Command.IfNotZero:
                if paper[ptr] == 0:
                    cmd_ptr += 1
            case Command.Exit:
                break

        cmd_ptr += 1


def interp(gt_map: dict[int, int], commands: list):
    paper = [0 for _ in range(PAPER_LENGTH)]
    process_command_list(paper, commands, gt_map)
