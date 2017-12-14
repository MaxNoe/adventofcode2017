from . import get_input


def parse_input(inp):
    def parse_line(line):
        k, v = line.split(' <-> ')
        v = set(map(int, v.split(',')))
        k = int(k)
        return k, v

    return dict(map(parse_line, inp.splitlines()))


def main():
    inp = get_input(12)

    pipes = parse_input(inp)


if __name__ == "__main__":
    main()
