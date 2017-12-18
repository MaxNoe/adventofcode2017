from . import get_input
from collections import defaultdict
from queue import Queue, Empty


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


def send_recv(instructions):
    queues = (Queue(), Queue())

    finished = [False, False]
    waiting = [False, False]
    n_sent = [0, 0]

    positions = [0, 0]
    registers = [defaultdict(int), defaultdict(int)]
    registers[1]['p'] = 1

    while not (all(waiting) or all(finished)):

        for program in [1, 0]:
            if positions[program] < 0 or positions[program] > len(instructions):
                finished[program] = True

            instruction, args = instructions[positions[program]]
            args = args.copy()

            register = registers[program]

            if len(args) > 1 and isinstance(args[1], str):
                args[1] = register[args[1]]

            if instruction == 'set':
                register[args[0]] = args[1]
            elif instruction == 'add':
                register[args[0]] += args[1]
            elif instruction == 'mul':
                register[args[0]] *= args[1]
            elif instruction == 'mod':
                register[args[0]] = register[args[0]] % args[1]

            elif instruction == 'rcv':
                try:
                    register[args[0]] = queues[program].get_nowait()
                    waiting[program] = False
                except Empty:
                    waiting[program] = True
                    continue

            if isinstance(args[0], str):
                args[0] = register[args[0]]

            if instruction == 'snd':
                queues[not program].put(args[0])
                n_sent[program] += 1

            if instruction == 'jgz' and args[0] > 0:
                positions[program] += args[1]
                continue

            positions[program] += 1

    return n_sent[1]


def main():
    inp = get_input(18)
    instructions = parse_input(inp)

    print('Task 1:', get_first_recovered_freq(instructions))
    print('Task 2:', send_recv(instructions))


if __name__ == "__main__":
    main()
