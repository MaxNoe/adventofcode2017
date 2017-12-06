from . import get_input
import math


def parse_input(inp):
    return list(map(int, inp.split()))


def redistribute_blocks(blocks):
    blocks = blocks.copy()
    n_banks = len(blocks)
    max_blocks = max(blocks)
    max_bank = blocks.index(max_blocks)

    redistribute_blocks = math.ceil(max_blocks / n_banks)
    n_last = max_blocks - redistribute_blocks * (n_banks - 1)

    for i in range(1, n_banks):
        idx = (max_bank + i) % n_banks
        blocks[idx] += max_blocks // (n_banks - 1)

    blocks[max_bank] = n_last

    return blocks


def count_cycles(memory_blocks):
    states = set()

    current_state = tuple(memory_blocks)
    cycles = 0
    while current_state not in states:
        states.add(current_state)

        memory_blocks = redistribute_blocks(memory_blocks)
        current_state = tuple(memory_blocks)

        cycles += 1

    return cycles


def main():
    inp = get_input(6)
    memory_blocks = parse_input(inp)

    print('Task 1', count_cycles(memory_blocks))


if __name__ == '__main__':
    main()
