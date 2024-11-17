from parse import CMDS

PAPER_LENGTH: int = 30_000


def process_command_list(paper: list[int], commands: list, goto_map: dict[int, int]):
    LAST_PAPER_IDX = PAPER_LENGTH - 1
    NUM_COMMANDS = len(commands)
    ptr: int = 0
    cmd_ptr: int = 0

    while cmd_ptr < NUM_COMMANDS:
        command = commands[cmd_ptr]

        match type(command):
            case CMDS.Forward:
                ptr = ptr + 1 if ptr < LAST_PAPER_IDX else 0
            case CMDS.Backward:
                ptr = ptr - 1 if ptr > 0 else LAST_PAPER_IDX
            case CMDS.Jump:
                ptr = command.val % PAPER_LENGTH
            case CMDS.Flip:
                paper[ptr] = int(not paper[ptr])
            case CMDS.Print:
                left = ptr
                right = ptr + (paper[ptr:] + [0]).index(0)
                print(bytes(paper[left:right]).decode("UTF-8"), end="")
            case CMDS.Inc:
                paper[ptr] += 1
            case CMDS.Dec:
                paper[ptr] -= 1
            case CMDS.Set:
                paper[ptr] = command.val
            case CMDS.GoTo:
                cmd_ptr = goto_map[command.val] - 1
            case CMDS.IfEq:
                if paper[ptr] != command.val:
                    cmd_ptr += 1
            case CMDS.IfNotZero:
                if paper[ptr] == 0:
                    cmd_ptr += 1
            case CMDS.Exit:
                break

        cmd_ptr += 1


def interp(gt_map: dict[int, int], commands: list):
    paper = [0 for _ in range(PAPER_LENGTH)]
    process_command_list(paper, commands, gt_map)
