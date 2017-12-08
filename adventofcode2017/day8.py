from . import get_input
from collections import defaultdict
import operator
from collections import namedtuple

Instruction = namedtuple('Instruction', ['register', 'operation', 'value', 'condition'])
Condition = namedtuple('Condition', ['register', 'operator', 'value'])


operator_mapping = {
    'inc': operator.add,
    'dec': operator.sub,
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '>': operator.gt,
}


def parse_input(inp):

    def parse_instruction(line):
        elements = line.strip().split()

        return Instruction(
            elements[0],
            elements[1],
            int(elements[2]),
            Condition(
                elements[4],
                elements[5],
                int(elements[6])
            )

        )

    return list(map(parse_instruction, inp.splitlines()))


def apply_instruction(instruction, registers):
    i = instruction
    c = i.condition
    if operator_mapping[c.operator](registers[c.register], c.value):

        registers[i.register] = operator_mapping[i.operation](
            registers[i.register], i.value
        )


def main():
    my_input = get_input(8)
    instructions = parse_input(my_input)

    registers = defaultdict(int)

    all_time_max = -1
    for instruction in instructions:
        apply_instruction(instruction, registers)

        all_time_max = max(all_time_max, max(registers.values()))

    print('Task 1:', max(registers.values()))
    print('Task 2:', all_time_max)


if __name__ == '__main__':
    main()
