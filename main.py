from parse import ParserException, parse
from interp import interp
from cli import CommandLineArgs, CommandParseException

def main():
    try:
        args = CommandLineArgs()
    except CommandParseException as e:
        e.display()
        return

    with open(args.file, "r") as file:
        file_content = file.read()
        try:
            gt_map, commands = parse(file_content)
            interp(gt_map, commands)

        except ParserException as e:
            e.display() 

if __name__ == "__main__":
    main()
