from . import get_input
from functools import reduce
from operator import xor


def parse_input(inp):
    return list(map(int, inp.split(',')))


def input_to_lengths(inp):
    return list(map(ord, inp))


def elf_hash(inp):
    lengths = input_to_lengths(inp) + [17, 31, 73, 47, 23]

    index = 0
    skip_size = 0
    elements = list(range(256))
    for _ in range(64):
        for length in lengths:
            index, skip_size = do_twist(elements, index, length, skip_size)
    dense_hash = to_dense_hash(elements)
    return to_hex_string(dense_hash)


def to_dense_hash(elements):
    return [
        reduce(xor, elements[i * 16: (i + 1) * 16])
        for i in range(16)
    ]


def to_hex_string(dense_hash):
    return ''.join(map(lambda i: f'{i:02x}', dense_hash))


def do_twist(elements, index, length, skip_size):
    start = index
    end = index + length
    n_wrapped = end - len(elements)

    selected = elements[start:end]
    if n_wrapped > 0:
        selected.extend(elements[:n_wrapped])

    selected.reverse()

    for i in range(length):
        idx = (index + i) % len(elements)
        elements[idx] = selected[i]

    index = (index + skip_size + length) % len(elements)
    skip_size += 1

    return index, skip_size


def main():
    inp = get_input(10)
    lengths = parse_input(inp)
    skip_size = 0
    index = 0
    elements = list(range(256))

    for length in lengths:
        index, skip_size = do_twist(elements, index, length, skip_size)

    print('Task 1', elements[0] * elements[1])
    print('Task 2', elf_hash(inp))


if __name__ == '__main__':
    main()
