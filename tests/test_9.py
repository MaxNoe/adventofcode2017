
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


