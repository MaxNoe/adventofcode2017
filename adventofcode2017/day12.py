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


def find_number_of_groups(pipes):
    checked = set()
    groups = 0
    for i in range(len(pipes)):
        if i in checked:
            continue

        groups += 1
        group = find_group(i, pipes)
        for p in group:
            checked.add(p)

    return groups


def main():
    inp = get_input(12)
    pipes = parse_input(inp)

    group_zero = find_group(0, pipes)
    print('Task 1:', len(group_zero))

    print('Task 2:', find_number_of_groups(pipes))


if __name__ == "__main__":
    main()
