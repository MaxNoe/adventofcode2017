inp = '''
0: 3
1: 2
4: 4
6: 4
'''.strip()


layers = {
    0: 3,
    1: 2,
    4: 4,
    6: 4,
}


def test_parse_input():
    from adventofcode2017.day13 import parse_input

    assert parse_input(inp) == layers


def test_zickzack():
    from adventofcode2017.day13 import zickzack

    z = zickzack(3)
    assert next(z) == 0
    assert next(z) == 1
    assert next(z) == 2
    assert next(z) == 1
    assert next(z) == 0
    assert next(z) == 1


def test_severity():
    from adventofcode2017.day13 import calc_severity

    assert calc_severity(layers) == 24


def test_delay():
    from adventofcode2017.day13 import calc_delay

    assert calc_delay(layers) == 10
