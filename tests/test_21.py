inp = '''../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
'''

rules = {
    ('..', '.#'): ('##.', '#..', '...'),
    ('.#.', '..#', '###'): ('#..#', '....', '....', '#..#'),
}


def test_parse():
    from adventofcode2017.day21 import parse_input
    assert parse_input(inp) == rules


def test_enhance():
    from adventofcode2017.day21 import enhance

    img = (
        '.#.',
        '..#',
        '###',
    )

    result = enhance(img, rules)
    assert result == (
        '#..#',
        '....',
        '....',
        '#..#',
    )

    result = enhance(result, rules)
    assert result == (
        '##.##.',
        '#..#..',
        '......',
        '##.##.',
        '#..#..',
        '......',
    )
