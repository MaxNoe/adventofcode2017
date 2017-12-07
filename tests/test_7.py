inp = '''
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
'''

parsed = [
    ('pbga', 66, []),
    ('xhth', 57, []),
    ('ebii', 61, []),
    ('havc', 66, []),
    ('ktlj', 57, []),
    ('fwft', 72, ['ktlj', 'cntj', 'xhth']),
    ('qoyq', 66, []),
    ('padx', 45, ['pbga', 'havc', 'qoyq']),
    ('tknk', 41, ['ugml', 'padx', 'fwft']),
    ('jptl', 61, []),
    ('ugml', 68, ['gyxo', 'ebii', 'jptl']),
    ('gyxo', 61, []),
    ('cntj', 57, []),
]


tree = {
    'tknk': {
        'ugml': {'gyxo': {}, 'ebii': {}, 'jptl': {}},
        'padx': {'pbga': {}, 'havc': {}, 'qoyq': {}},
        'fwft': {'ktlj': {}, 'cntj': {}, 'xhth': {}},
    },
}


def test_parse_input():
    from adventofcode2017.day7 import parse_input

    assert parse_input(inp) == parsed


def test_find_root():

    from adventofcode2017.day7 import find_root

    assert find_root(parsed) == 'tknk'


def test_build_tree():

    from adventofcode2017.day7 import build_tree

    assert build_tree(parsed) == tree
