def test_parse_input():
    from adventofcode2017.day6 import parse_input

    nums = [0, 2, 7, 0]
    inp = '\t'.join(map(str, nums))
    assert parse_input(inp) == nums
