from . import get_input
from collections import defaultdict


def parse_input(inp):
    return list(map(int, inp.split()))


def redistribute_blocks(blocks):
    blocks = blocks.copy()
    n_banks = len(blocks)
    max_blocks = max(blocks)
    max_bank = blocks.index(max_blocks)

    blocks[max_bank] = 0

    idx = (max_bank + 1) % n_banks

    while max_blocks > 0:
        blocks[idx] += 1
        max_blocks -= 1
        idx = (idx + 1) % n_banks

    return blocks


def count_cycles(memory_blocks, return_loop_size=False):

    states = defaultdict(int)
    current_state = tuple(memory_blocks)
    cycle = 0

    while current_state not in states:
        states[current_state] = cycle

        memory_blocks = redistribute_blocks(memory_blocks)

        current_state = tuple(memory_blocks)

        cycle += 1

    if return_loop_size is False:
        return cycle
    return cycle, cycle - states[current_state]


def main():
    inp = get_input(6)
    memory_blocks = parse_input(inp)

    cycles, loop_size = count_cycles(memory_blocks, return_loop_size=True)
    print('Task 1: ', cycles)
    print('Task 2: ', loop_size)


if __name__ == '__main__':
    main()
