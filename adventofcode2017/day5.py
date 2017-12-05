from . import get_input


def parse_input(inp):
    return list(map(int, inp.split()))


def do_step(position, instructions):
    instructions = instructions.copy()

    steps = instructions[position]
    instructions[position] += 1
    position += steps

    return position, instructions


def count_steps(instructions):
    position = 0

    steps = 0
    while position < len(instructions):
        position, instructions = do_step(position, instructions)
        steps += 1
    return steps


def main():
    my_input = get_input(5)
    instructions = parse_input(my_input)


if __name__ == '__main__':
    main()
