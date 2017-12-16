from . import get_input
from itertools import cycle


def parse_input(inp):
    return {
        int(k): int(v)
        for k, v in map(lambda s: s.split(':'), inp.splitlines())
    }


def init_firewall(layers):
    firewall = {
        depth: {'period': 2 * (size - 1), 'size': size}
        for depth, size in layers.items()
    }
    return firewall


def calc_severity(layers, delay=0):
    firewall = init_firewall(layers)

    return sum(
        depth * d['size']
        for depth, d in firewall.items()
        if (depth + delay) % d['period'] == 0
    )


def check_caught(firewall, delay=0):
    return any(
        (depth + delay) % d['period'] == 0
        for depth, d in firewall.items()
    )


def calc_delay(layers):
    delay = 0
    firewall = init_firewall(layers)
    while True:
        if not check_caught(firewall, delay):
            break
        delay += 1
    return delay


def main():
    inp = get_input(13)
    layers = parse_input(inp)

    print('Task 1:', calc_severity(layers))
    print('Task 2:', calc_delay(layers))


if __name__ == "__main__":
    main()
