
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


def test_garbage():
    from adventofcode2017.day9 import calc_score

    assert calc_score('<>', count_garbage=True)[1] == 0
    assert calc_score('<random characters>', count_garbage=True)[1] == 17
    assert calc_score('<<<<>', count_garbage=True)[1] == 3
    assert calc_score('<{!>}>', count_garbage=True)[1] == 2
    assert calc_score('<!!>', count_garbage=True)[1] == 0
    assert calc_score('<!!!>>', count_garbage=True)[1] == 0
    assert calc_score('<{o"i!a,<{i<a>', count_garbage=True)[1] == 10
