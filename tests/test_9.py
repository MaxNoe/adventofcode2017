def test_num_groups():
    from adventofcode2017.day9 import num_groups

    assert num_groups([]) == 1
    assert num_groups([[], [], []]) == 4
    assert num_groups([[[]]]) == 3


def test_parse_groups():
    from adventofcode2017.day9 import parse_into_groups, num_groups

    groups = parse_into_groups('{}')
    assert num_groups(groups) == 1

    groups = parse_into_groups('{{{}}}')
    assert num_groups(groups) == 3

    groups = parse_into_groups('{{{},{},{{}}}}')
    assert num_groups(groups) == 3

    groups = parse_into_groups('{<{},{},{{}}>}')
    assert num_groups(groups) == 1

    groups = parse_into_groups('{<a>,<a>,<a>,<a>}')
    assert num_groups(groups) == 1

    groups = parse_into_groups('{{<a>},{<a>},{<a>},{<a>}}')
    assert num_groups(groups) == 5

    groups = parse_into_groups('{{<!>},{<!>},{<!>},{<a>}}')
    assert num_groups(groups) == 2


def test_score():
    from adventofcode2017.day9 import calc_score

    assert calc_score('{}') == 1
    assert calc_score('{{{}}}') == 6
    assert calc_score('{{},{}}') == 5
    assert calc_score('{{{},{},{{}}}}') == 16
    assert calc_score('{<a>,<a>,<a>,<a>}') == 1
    assert calc_score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
    assert calc_score('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
    assert calc_score('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3
