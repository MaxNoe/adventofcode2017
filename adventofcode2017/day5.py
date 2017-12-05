from . import get_input


def parse_input(inp):
    return list(map(int, inp.split()))


def main():
    my_input = get_input(5)
    instructions = parse_input(my_input)


if __name__ == '__main__':
    main()
