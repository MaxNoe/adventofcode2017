from . import get_input

import re


def parse_input(inp):

    program = {'states': {}}

    for line in inp.splitlines():
        line = line.strip()
        if not line:
            continue

        m = re.match(r'Begin in state ([A-Z])', line)
        if m:
            program['initial_state'] = m.groups()[0]
            continue

        m = re.match(r'.*after (\d+) steps\.', line)
        if m:
            program['steps'] = int(m.groups()[0])
            continue

        m = re.match('In state ([A-Z]):', line)
        if m:
            current_state = m.groups()[0]
            program['states'][current_state] = []
            continue

        m = re.match('If the current value is [01]:', line)
        if m:
            current_instructions = []
            program['states'][current_state].append(current_instructions)
            continue

        m = re.match('- Write the value ([01])', line)
        if m:
            current_instructions.append(('write', int(m.groups()[0])))
            continue

        m = re.match('- Move one slot to the ([a-z]+).', line)
        if m:
            direction = m.groups()[0]
            if direction == 'left':
                direction = -1
            elif direction == 'right':
                direction = 1
            current_instructions.append(('move', direction))
            continue

        m = re.match('- Continue with state ([A-Z]).', line)
        if m:
            state = m.groups()[0]
            current_instructions.append(('continue', state))

    return program


def calc_checksum(program):
    tape = {}
    pos = 0

    state = program['initial_state']
    for i in range(program['steps']):

        instructions = program['states'][state][tape.get(pos, 0)]
        for instruction, arg in instructions:
            if instruction == 'write':
                tape[pos] = arg
            elif instruction == 'move':
                pos += arg
            elif instruction == 'continue':
                state = arg
                continue

    return sum(tape.values())


def main():
    program = parse_input(get_input(25))
    print('Task 1:', calc_checksum(program))


if __name__ == "__main__":
    main()
