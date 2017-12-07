from . import get_input
import re
from collections import namedtuple

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


def main():
    my_input = get_input(7)
    programs = parse_input(my_input)

    print('Task 1:', find_root(programs).name)


if __name__ == '__main__':
    main()

