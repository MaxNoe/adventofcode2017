inp = '''..#
#..
...
'''



def test_parse_inp():
    from adventofcode2017.day22 import parse_input
    infected = {(1, 1), (-1, 0)}
    assert parse_input(inp) == infected


def test_do_burst():
    from adventofcode2017.day22 import do_burst

    infected = {(1, 1), (-1, 0)}
    direction = (0, 1)
    position = (0, 0)

    position, direction, new_infection = do_burst(position, direction, infected)
    assert direction == (-1, 0)
    assert position == (-1, 0)
    assert (0, 0) in infected
    assert new_infection

    position, direction, new_infection = do_burst(position, direction, infected)
    assert direction == (0, 1)
    assert position == (-1, 1)
    assert (-1, 0) not in infected
    assert not new_infection


def test_70():
    from adventofcode2017.day22 import do_burst

    infected = {(1, 1), (-1, 0)}
    direction = (0, 1)
    position = (0, 0)

    n_infections = 0
    for i in range(70):
        position, direction, new_infection = do_burst(position, direction, infected)
        n_infections += new_infection

    assert direction == (0, 1)
    assert n_infections == 41


def test_10000():
    from adventofcode2017.day22 import do_burst

    infected = {(1, 1), (-1, 0)}
    direction = (0, 1)
    position = (0, 0)

    n_infections = 0
    for i in range(10000):
        position, direction, new_infection = do_burst(position, direction, infected)
        n_infections += new_infection

    assert n_infections == 5587
