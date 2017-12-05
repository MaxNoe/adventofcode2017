inp = '''0
3
0
1
-3
'''


def test_parse_input():

    from adventofcode2017.day5 import parse_input

    assert parse_input(inp) == [0, 3, 0, 1, -3]


def test_steps():
    from adventofcode2017.day5 import parse_input, do_step

    instructions = parse_input(inp)

    position = 0
    position, instructions = do_step(position, instructions)

    assert position == 0, 'Wrong position after step 1'
    assert instructions[0] == 1, 'Wrong instruction set after step 1'

    position, instructions = do_step(position, instructions)
    assert position == 1, 'Wrong position after step 2'
    assert instructions[0] == 2, 'Wrong instruction set after step 2'

    position, instructions = do_step(position, instructions)
    assert position == 4, 'Wrong position after step 3'
    assert instructions[1] == 4, 'Wrong instruction set after step 3'

    position, instructions = do_step(position, instructions)
    assert position == 1, 'Wrong position after step 4'
    assert instructions[4] == -2, 'Wrong instruction set after step 4'

    position, instructions = do_step(position, instructions)
    assert position == 5, 'Wrong position after step 5'
    assert instructions[1] == 5, 'Wrong instruction set after step 5'


def test_count_steps():
    from adventofcode2017.day5 import parse_input, count_steps

    instructions = parse_input(inp)

    assert count_steps(instructions) == 5
