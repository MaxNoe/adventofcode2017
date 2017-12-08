inp = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
'''

parsed = [
    ('b', 'inc', 5, ('a', '>', 1)),
    ('a', 'inc', 1, ('b', '<', 5)),
    ('c', 'dec', -10, ('a', '>=', 1)),
    ('c', 'inc', -20, ('c', '==', 10)),
]


def test_parse_input():
    from adventofcode2017.day8 import parse_input

    assert parse_input(inp) == parsed


