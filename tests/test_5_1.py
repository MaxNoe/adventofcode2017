inp = '''0
3
0
1
-3
'''


def test_parse_input():

    from adventofcode2017.day5 import parse_input

    assert parse_input(inp) == [0, 3, 0, 1, -3]


def test_jumps():
    from adventofcode2017.day5 import parse_input, do_step

    instructions = parse_input(inp)

    position = 0
    do_step(position, instructions)

    assert position == 0, 'Wrong position after step 1'
    assert instructions[0] == 1, 'Wrong instruction set after step 1'

    do_step(position, instructions)
    assert position == 1, 'Wrong position after step 2'
    assert instructions[0] == 2, 'Wrong instruction set after step 2'

    do_step(position, instructions)
    assert position == 4, 'Wrong position after step 3'
    assert instructions[1] == 4, 'Wrong instruction set after step 3'

    do_step(position, instructions)
    assert position == 1, 'Wrong position after step 4'
    assert instructions[4] == -2, 'Wrong instruction set after step 4'

    do_step(position, instructions)
    assert position == 5, 'Wrong position after step 5'
    assert instructions[1] == 5, 'Wrong instruction set after step 5'


def test_count_jumps():
    from adventofcode2017.day5 import parse_input, count_jumps

    instructions = parse_input(inp)

    assert count_jumps(instructions) == 5
