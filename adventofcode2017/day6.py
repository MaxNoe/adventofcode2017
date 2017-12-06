from . import get_input


def parse_input(inp):
    return list(map(int, inp.split()))


def main():
    inp = get_input(6)
    memory_blocks = parse_input(inp)
    print(memory_blocks)


if __name__ == '__main__':
    main()
