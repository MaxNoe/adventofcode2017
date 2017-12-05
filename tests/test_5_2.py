inp = '''0
3
0
1
-3
'''


def test_steps():
    from adventofcode2017.day5 import parse_input
    from adventofcode2017.day5_ext import do_step_2

    instructions = parse_input(inp)

    position = 0
    for i in range(10):
        position, instructions = do_step_2(position, instructions)

    assert instructions == [2, 3, 2, 3, -1]


def test_count_steps():
    from adventofcode2017.day5 import parse_input, count_steps

    instructions = parse_input(inp)

    assert count_steps(instructions, puzzle2=True) == 10
