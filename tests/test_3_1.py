def test_manhattan():
    from adventofcode2017.day3 import manhattan_spiral

    assert manhattan_spiral(1) == 0
    assert manhattan_spiral(12) == 3
    assert manhattan_spiral(15) == 2
    assert manhattan_spiral(23) == 2
    assert manhattan_spiral(1024) == 31


def test_spiral():
    from adventofcode2017.day3 import address2ring

    assert address2ring(1) == 0
    assert address2ring(2) == 1
    assert address2ring(9) == 1
    assert address2ring(10) == 2
    assert address2ring(25) == 2
    assert address2ring(26) == 3


if __name__ == '__main__':
    test_manhattan()
