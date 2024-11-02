from parse import parse
from interp import interp
import sys

def main():
    with open(sys.argv[1], "r") as f:
        gt_map, commands = parse(f.read())
        interp(gt_map, commands)


if __name__ == "__main__":
    main()
