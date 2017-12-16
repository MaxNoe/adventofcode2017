inp = 's1,x3/4,pe/b'


def test_input():
    from adventofcode2017.day16 import parse_input

    assert parse_input(inp) == [('s', 1), ('x', 3, 4), ('p', 'e', 'b')]



def test_dance():
    from adventofcode2017.day16 import spin_programs, swap_indices, swap_names
    programs = list('abcde')

    spin_programs(programs, 1)
    assert programs == list('eabcd')

    swap_indices(programs, 3, 4)
    assert programs == list('eabdc')

    swap_names(programs, 'e', 'b')
    assert programs == list('baedc')
