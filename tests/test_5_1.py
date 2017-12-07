inp = '''0
3
0
1
-3
'''


def test_parse_input():

    from adventofcode2017.day5 import parse_input

    assert parse_input(inp) == [0, 3, 0, 1, -3]


def test_count_steps():
    from adventofcode2017.day5 import parse_input, count_steps

    instructions = parse_input(inp)

    assert count_steps(instructions) == 5
