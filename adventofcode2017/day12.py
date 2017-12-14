from . import get_input


def parse_input(inp):
    def parse_line(line):
        k, v = line.split(' <-> ')
        v = set(map(int, v.split(',')))
        k = int(k)
        return k, v

    return dict(map(parse_line, inp.splitlines()))


def find_group(root, pipes, group=None):
    if group is None:
        group = set()
    group.add(root)
    for connected in pipes[root]:
        if connected not in group:
            for g in find_group(connected, pipes, group):
                group.add(g)

    return group


def main():
    inp = get_input(12)
    pipes = parse_input(inp)

    group_zero = find_group(0, pipes)
    print('Task 1:', len(group_zero))


if __name__ == "__main__":
    main()
