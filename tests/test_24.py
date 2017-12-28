inp = '''0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
'''

components = [
    (0, 2),
    (2, 2),
    (2, 3),
    (3, 4),
    (3, 5),
    (0, 1),
    (10, 1),
    (9, 10),
]

bridges = [
    ((0, 1), ),
    ((0, 1), (10, 1)),
    ((0, 1), (10, 1), (9, 10)),
    ((0, 2), ),
    ((0, 2), (2, 3)),
    ((0, 2), (2, 3), (3, 4)),
    ((0, 2), (2, 3), (3, 5)),
    ((0, 2), (2, 2)),
    ((0, 2), (2, 2), (2, 3)),
    ((0, 2), (2, 2), (2, 3), (3, 4)),
    ((0, 2), (2, 2), (2, 3), (3, 5)),
]


def test_parse():
    from adventofcode2017.day24 import parse_input
    assert parse_input(inp) == components


def test_strength():
    from adventofcode2017.day24 import calc_strength

    bridge = [(0, 3), (3, 7), (7, 4)]
    assert calc_strength(bridge) == 24


def test_valid_bridges():
    from adventofcode2017.day24 import build_bridges
    my_bridges = build_bridges(components)

    my_bridges = set(map(tuple, my_bridges))
    assert my_bridges == set(bridges)


def test_best_bridge():
    from adventofcode2017.day24 import find_best_bridge, calc_strength, build_bridges

    bridges = build_bridges(components)
    assert find_best_bridge(bridges) == [(0, 1), (10, 1), (9, 10)]
    assert calc_strength(find_best_bridge(bridges)) == 31


def test_longest():
    from adventofcode2017.day24 import find_longest_bridge, calc_strength, build_bridges

    bridges = build_bridges(components)
    assert find_longest_bridge(bridges) == [(0, 2), (2, 2), (2, 3), (3, 5)]
    assert calc_strength(find_longest_bridge(bridges)) == 19
