from adventofcode2017.day20 import Vector, Particle

inp = '''
p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
'''.strip()

particles = [
    Particle(0, Vector(3, 0, 0), Vector(2, 0, 0), Vector(-1, 0, 0)),
    Particle(1, Vector(4, 0, 0), Vector(0, 0, 0), Vector(-2, 0, 0)),
]


def test_parse_input():
    from adventofcode2017.day20 import parse_input
    assert parse_input(inp) == particles


def find_slowest_particle():
    from adventofcode2017.day20 import find_slowest_particle

    assert find_slowest_particle(particles) == 0
