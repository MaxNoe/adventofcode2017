from . import get_input
from collections import defaultdict


def parse_input(inp):
    def parse_line(line):
        inst, *args = line.split()
        try:
            args[0] = int(args[0])
        except ValueError:
            pass

        if len(args) == 2:
            try:
                args[1] = int(args[1])
            except ValueError:
                pass
        return inst, args
    return list(map(parse_line, inp.splitlines()))


def get_first_recovered_freq(instructions):
    pos = 0
    last_played = None
    registers = defaultdict(int)

    while 0 <= pos < len(instructions):
        instruction, args = instructions[pos]
        args = args.copy()

        if len(args) > 1 and isinstance(args[1], str):
            args[1] = registers[args[1]]

        if instruction == 'set':
            registers[args[0]] = args[1]
        elif instruction == 'add':
            registers[args[0]] += args[1]
        elif instruction == 'mul':
            registers[args[0]] *= args[1]
        elif instruction == 'mod':
            registers[args[0]] = registers[args[0]] % args[1]
        elif instruction == 'snd':
            last_played = registers[args[0]]
        elif instruction == 'rcv':
            if registers[args[0]] != 0:
                break

        if isinstance(args[0], str):
            args[0] = registers[args[0]]

        if instruction == 'jgz' and args[0] > 0:
            pos += args[1]
        else:
            pos += 1

    return last_played


def main():
    inp = get_input(18)
    instructions = parse_input(inp)

    print('Task 1:', get_first_recovered_freq(instructions))



if __name__ == "__main__":
    main()
