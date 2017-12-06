nums = [0, 2, 7, 0]


def test_parse_input():
    from adventofcode2017.day6 import parse_input

    inp = '\t'.join(map(str, nums))
    assert parse_input(inp) == nums


def test1():
    from adventofcode2017.day6 import redistribute_blocks

    result = redistribute_blocks(nums)
    assert result == [2, 4, 1, 2]

    result = redistribute_blocks(result)
    assert result == [3, 1, 2, 3]

    result = redistribute_blocks(result)
    assert result == [0, 2, 3, 4]

    result = redistribute_blocks(result)
    assert result == [1, 3, 4, 1]

    result = redistribute_blocks(result)
    assert result == [2, 4, 1, 2]


def test2():
    from adventofcode2017.day6 import count_cycles

    assert count_cycles(nums) == 5


def test3():
    from adventofcode2017.day6 import count_cycles

    assert count_cycles(nums, return_loop_size=True) == (5, 4)
