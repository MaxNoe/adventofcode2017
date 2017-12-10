inp = '3, 4, 1, 5'
lengths = [3, 4, 1, 5]


def test_parse_input():
    from adventofcode2017.day10 import parse_input

    assert parse_input(inp) == lengths


def test_do_twist():
    from adventofcode2017.day10 import do_twist

    index = 0
    skip_size = 0
    elements = list(range(5))

    index, skip_size = do_twist(elements, index, lengths[0], skip_size)
    assert elements == [2, 1, 0, 3, 4]
    assert index == 3
    assert skip_size == 1

    index, skip_size = do_twist(elements, index, lengths[1], skip_size)
    assert elements == [4, 3, 0, 1, 2]
    assert index == 3
    assert skip_size == 2

    index, skip_size = do_twist(elements, index, lengths[2], skip_size)
    assert elements == [4, 3, 0, 1, 2]
    assert index == 1
    assert skip_size == 3

    index, skip_size = do_twist(elements, index, lengths[3], skip_size)
    assert elements == [3, 4, 2, 1, 0]
    assert index == 4
    assert skip_size == 4
