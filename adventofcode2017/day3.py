from . import get_input


def manhattan(x, y):
    return abs(x) + abs(y)


def ring_size(ring):
    return max_address_ring(ring) - max_address_ring(ring - 1)


def min_address_ring(ring):
    return max_address_ring(ring - 1) + 1


def max_address_ring(ring):
    return edge_length(ring)**2


def address2ring(address):
    s = 1
    ring = 0
    while s < address:
        ring += 1
        s += ring_size(ring)
    return ring


def edge_length(ring):
    return 2 * ring + 1


def pos2edge(pos, ring):
    l = edge_length(ring)

    if ring == 0:
        return 0

    if pos < l - 2:
        return 0

    if pos < 2 * l - 2:
        return 1

    if pos < 3 * l - 2:
        return 2

    return 3


def address2xy(address):
    r = address2ring(address)
    if r == 0:
        return (0, 0)

    min_addr = min_address_ring(r)
    pos_in_ring = address - min_addr

    x0 = r
    y0 = -r + 1

    edge = pos2edge(pos_in_ring, r)

    l = edge_length(r)

    if edge == 0:
        return (x0, y0 + pos_in_ring)

    if edge == 1:
        return (x0 - (pos_in_ring - (l - 2)), r)

    if edge == 2:
        return (-r, r - (pos_in_ring - (2 * l - 3)))

    if edge == 3:
        return (-r + pos_in_ring - (3 * l - 4), -r)


def manhattan_spiral(address):
    x, y = address2xy(address)
    return manhattan(x, y)


def main():
    address = int(get_input(3))
    print(manhattan_spiral(address))


if __name__ == '__main__':
    main()
