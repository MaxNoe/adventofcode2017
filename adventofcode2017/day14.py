from . import get_input
from .day10 import elf_hash
from collections import deque


def hex2bin(num):

    s = ''
    for n in num:
        h = int(n, base=16)
        b = '{:04b}'.format(h)
        s += b
    return list(map(int, s))


def knothash(inp, row):
    inp = inp + '-{}'.format(row)
    return hex2bin(elf_hash(inp))


def parse_memory(inp):
    return [knothash(inp, i) for i in range(128)]


def calc_n_used(memory):
    return sum(sum(r) for r in memory)


directions = [
    (-1, 0), (0, -1), (0, 1), (1, 0)
]


def find_regions(memory):
    visited = set()
    to_check = deque()
    regions = []

    for row in range(128):
        for col in range(128):
            if (row, col) in visited:
                continue

            visited.add((row, col))

            if memory[row][col] == 0:
                continue

            for dr, dc in directions:
                to_check.append((row + dr, col + dc))

            region = {(row, col)}
            while len(to_check) > 0:
                r, c = to_check.popleft()
                if r > 127 or r < 0 or c > 127 or c < 0:
                    continue
                if (r, c) in visited:
                    continue
                visited.add((r, c))

                if memory[r][c] == 1:
                    region.add((r, c))
                    for dr, dc in directions:
                        to_check.append((r + dr, c + dc))
            regions.append(region)
    return regions


def main():
    inp = get_input(14)
    memory = parse_memory(inp)

    print('Task 1:', calc_n_used(memory))
    print('Task 2:', len(find_regions(memory)))


if __name__ == "__main__":
    main()
