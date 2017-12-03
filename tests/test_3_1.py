def test_manhattan():
    from adventofcode2017.day3 import manhattan_spiral

    assert manhattan_spiral(1) == 0
    assert manhattan_spiral(12) == 3
    assert manhattan_spiral(23) == 2
    assert manhattan_spiral(1024) == 31
