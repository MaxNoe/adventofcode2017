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
    firewall = {
        depth: {'scanner': zickzack(size), 'size': size}
        for depth, size in layers.items()
    }
    update_firewall(firewall)
    return firewall


def update_firewall(firewall):
    for c in firewall.values():
        c['current_pos'] = next(c['scanner'])


def calc_severity(layers):
    firewall = init_firewall(layers)

    total_depth = max(layers.keys())
    print(total_depth)

    severity = 0
    for depth in range(total_depth + 1):
        print(depth, firewall.get(depth, {}).get('current_pos'))
        if depth in firewall:
            current_layer = firewall[depth]
            if current_layer['current_pos'] == 0:
                severity += depth * current_layer['size']
        update_firewall(firewall)

    return severity


def main():
    inp = get_input(13)
    layers = parse_input(inp)

    print('Task 1:', calc_severity(layers))


if __name__ == "__main__":
    main()
