from . import get_input
from itertools import cycle


def parse_input(inp):
    return {
        int(k): int(v)
        for k, v in map(lambda s: s.split(':'), inp.splitlines())
    }


def zickzack(n):
    return cycle(list(range(n)) + list(range(n - 2, 0, -1)))


def init_firewall(layers):
    return {
        depth: zickzack(size)
        for depth, size in layers.items()
    }


def main():
    inp = get_input(13)
    layers = parse_input(inp)
    firewall = init_firewall(layers)


if __name__ == "__main__":
    main()
