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


def address2xy(address):
    r = address2ring(address)
    if r == 0:
        return (0, 0)

    min_addr = min_address_ring(r)
    pos_in_ring = address - min_addr

    x0 = r
    y0 = -r + 1

    l = edge_length(r)

    if pos_in_ring < l - 2:
        return (x0, y0 + pos_in_ring)

    return (0, 0)


def manhattan_spiral(address):
    return manhattan(*address2xy(address))


def main():
    address = int(get_input(3))
    print(manhattan_spiral(address))


if __name__ == '__main__':
    main()
