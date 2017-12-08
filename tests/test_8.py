from collections import defaultdict


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


def test_instructions():
    from adventofcode2017.day8 import apply_instruction

    registers = defaultdict(int)

    apply_instruction(parsed[0], registers)
    assert registers['b'] == 0

    apply_instruction(parsed[1], registers)
    assert registers['a'] == 1

    apply_instruction(parsed[2], registers)
    assert registers['c'] == 10

    apply_instruction(parsed[3], registers)
    assert registers['c'] == -10
