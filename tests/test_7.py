inp = '''pbga (66)
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

from adventofcode2017.day7 import Program

programs = {
    'pbga': Program('pbga', 66, tuple()),
    'xhth': Program('xhth', 57, tuple()),
    'ebii': Program('ebii', 61, tuple()),
    'havc': Program('havc', 66, tuple()),
    'ktlj': Program('ktlj', 57, tuple()),
    'fwft': Program('fwft', 72, ('ktlj', 'cntj', 'xhth')),
    'qoyq': Program('qoyq', 66, tuple()),
    'padx': Program('padx', 45, ('pbga', 'havc', 'qoyq')),
    'tknk': Program('tknk', 41, ('ugml', 'padx', 'fwft')),
    'jptl': Program('jptl', 61, tuple()),
    'ugml': Program('ugml', 68, ('gyxo', 'ebii', 'jptl')),
    'gyxo': Program('gyxo', 61, tuple()),
    'cntj': Program('cntj', 57, tuple()),
}


tree = {
    'tknk': {
        'ugml': {'gyxo': {}, 'ebii': {}, 'jptl': {}},
        'padx': {'pbga': {}, 'havc': {}, 'qoyq': {}},
        'fwft': {'ktlj': {}, 'cntj': {}, 'xhth': {}},
    },
}


def test_parse_input():
    from adventofcode2017.day7 import parse_input

    assert parse_input(inp) == programs


def test_find_root():

    from adventofcode2017.day7 import find_root

    assert find_root(programs).name == 'tknk'


def test_build_tree():

    from adventofcode2017.day7 import build_tree

    assert build_tree(programs) == tree


def test_tree_weight():
    from adventofcode2017.day7 import calc_tree_weight

    assert calc_tree_weight('ugml', tree['tknk']['ugml'], programs) == 251
    assert calc_tree_weight('padx', tree['tknk']['padx'], programs) == 243
    assert calc_tree_weight('fwft', tree['tknk']['fwft'], programs) == 243


def test_find_wrong_weight():
    from adventofcode2017.day7 import find_corrected_weight

    assert find_corrected_weight(tree, programs) == 60
