from . import get_input


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


def count_cycles(memory_blocks):

    states = set()
    current_state = tuple(memory_blocks)
    cycle = 0
    while current_state not in states:

        states.add(current_state)

        memory_blocks = redistribute_blocks(memory_blocks)

        current_state = tuple(memory_blocks)

        cycle += 1

    return cycle


def main():
    inp = get_input(6)
    memory_blocks = parse_input(inp)

    print('Task 1', count_cycles(memory_blocks))


if __name__ == '__main__':
    main()
