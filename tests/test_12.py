inp = '''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
'''

pipes = {
    0: {2},
    1: {1},
    2: {0, 3, 4},
    3: {2, 4},
    4: {2, 3, 6},
    5: {6},
    6: {4, 5},
}


def test_parse_input():
    from adventofcode2017.day12 import parse_input

    assert parse_input(inp) == pipes


def test_group():
    from adventofcode2017.day12 import find_group

    assert find_group(0, pipes) == {0, 2, 3, 4, 5, 6}
