from . import get_input

from collections import namedtuple
from itertools import combinations
import re
import math
from collections import defaultdict

Particle = namedtuple('Particle', 'id p v a')


class Vector:
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return Vector(self.x + other, self.y + other, self.z + other)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return 'Vector(x={}, y={}, z={})'.format(self.x, self.y, self.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))


particle_re = re.compile('^p=<(.*)>, v=<(.*)>, a=<(.*)>$')


def parse_input(inp):
    def parse_line(i, line) :
        m = particle_re.match(line)
        p, a, v = map(lambda g: Vector(*map(int, g.split(','))), m.groups())
        return Particle(i, p, a, v)

    return [parse_line(i, l) for i, l in enumerate(inp.splitlines())]


def manhattan_abs(vector):
    return abs(vector.x) + abs(vector.y) + abs(vector.z)


def prop_particle(particle, time):
    a = particle.a
    p = particle.p
    v = particle.v

    p = p + v * time + 0.5 * a * time * (time + 1)
    v = v + a * time

    return Particle(particle.id, p, v, a)


def find_slowest_particle(particles):
    ps = [prop_particle(p, 1e9) for p in particles]
    ps.sort(key=lambda p: manhattan_abs(p.p))
    return ps[0].id


def remove_colliding(particles):
    particles = particles.copy()

    for t in range(1000):

        positions = defaultdict(set)
        for p in particles:
            positions[prop_particle(p, t).p].add(p)

        for pos, collided in filter(lambda s: len(s[1]) > 1, positions.items()):
            for p in collided:
                particles.remove(p)
    return particles


def main():
    inp = get_input(20)
    particles = parse_input(inp)

    print('Task 1:', find_slowest_particle(particles))

    print('Task 2:', len(remove_colliding(particles)))


if __name__ == "__main__":
    main()
