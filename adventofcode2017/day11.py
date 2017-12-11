from collections import Counter
from . import get_input


class CubePoint:
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        return (
            abs(self.x - other.x)
            + abs(self.y - other.y)
            + abs(self.z - other.z)
        ) / 2

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __mul__(self, other):
        return CubePoint(
            self.x * other,
            self.y * other,
            self.z * other,
        )


directions = {
    'n': CubePoint(0, 1, -1),
    'ne': CubePoint(1, 0, -1),
    'se': CubePoint(1, -1, 0),
    's': CubePoint(0, -1, 1),
    'sw': CubePoint(-1, 0, 1),
    'nw': CubePoint(-1, 1, 0),
}


def main():
    inp = get_input(11)

    c = Counter(inp.split(','))
    p = CubePoint(0, 0, 0)

    for direction, count in c.items():
        p += directions[direction] * count

    print('Task 1:', p.distance(CubePoint(0, 0, 0)))


if __name__ == '__main__':
    main()
