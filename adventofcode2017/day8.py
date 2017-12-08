from . import get_input
from collections import defaultdict


def parse_input(inp):

    def parse_instruction(line):
        elements = line.strip().split()

        return (
            elements[0],
            elements[1],
            int(elements[2]),
            (
                elements[4],
                elements[5],
                int(elements[6])
            )

        )

    return list(map(parse_instruction, inp.splitlines()))



def main():
    my_input = get_input(8)
    instructions = parse_input(my_input)


if __name__ == '__main__':
    main()
