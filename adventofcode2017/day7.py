from . import get_input
import re
from collections import namedtuple, defaultdict

tower_re = re.compile('^([a-z]+) [(]([0-9]+)[)](?: -> ([a-z, ]+))?$')


Program = namedtuple('Program', ['name', 'weight', 'children'])


def parse_input(inp):
    groups = map(lambda s: tower_re.match(s).groups(), inp.splitlines())
    return {
        c[0]: Program(c[0], int(c[1]), tuple(c[2].split(', ')) if c[2] else tuple())
        for c in groups
    }


def find_root(programs):
    child_nodes = set()
    for program in programs.values():
        for name in program.children:
            child_nodes.add(name)

    for name, program in programs.items():
        if name not in child_nodes and len(program.children) > 0:
            return program


def build_tree(programs):
    root = find_root(programs)
    children = find_children(root, programs)

    return {root.name: children}


def find_children(root, programs):
    tree = {}
    for name in root.children:
        child = programs[name]
        tree[name] = find_children(child, programs)
    return tree


def calc_tree_weight(root, tree, programs):
    root = programs[root]
    weight = root.weight
    for child in tree:
        weight += calc_tree_weight(child, tree[child], programs)
    return weight


def find_wrong_tree(tree, programs):
    weights = defaultdict(list)

    for root, subtree in tree.items():
        weight = calc_tree_weight(root, subtree, programs)
        weights[weight].append(root)

    for res in filter(lambda t: len(t[1]) == 1, weights.items()):
        return res[1][0]
    return None


def find_corrected_weight(tree, programs):

    wrong = find_wrong_tree(tree, programs)
    while wrong:
        last_tree = tree
        last_wrong = wrong

        tree = tree[wrong]
        wrong = find_wrong_tree(tree, programs)

    for key in last_tree:
        if key != last_wrong:
            break

    correct_weight = calc_tree_weight(key, last_tree[key], programs)
    wrong_weight = calc_tree_weight(last_wrong, last_tree[last_wrong], programs)

    return programs[last_wrong].weight - (wrong_weight - correct_weight)


def main():
    my_input = get_input(7)
    programs = parse_input(my_input)

    print('Task 1:', find_root(programs).name)

    tree = build_tree(programs)

    print('Task 2:', find_corrected_weight(tree, programs))


if __name__ == '__main__':
    main()
