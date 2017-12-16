from . import get_input
import string


def parse_input(inp):
    def parse_item(item):
        command = item[0]
        if command == 's':
            return ('s', int(item[1:]))
        elif command == 'p':
            return ('p', *item[1:].split('/'))
        elif command == 'x':
            return ('x', *map(int, item[1:].split('/')))

    return list(map(parse_item, inp.split(',')))


def spin_programs(programs, amount):
    for i in range(amount):
        programs.insert(0, programs.pop())


def swap_indices(programs, i1, i2):
    programs[i1], programs[i2] = programs[i2], programs[i1]


def swap_names(programs, n1, n2):
    i1 = programs.index(n1)
    i2 = programs.index(n2)
    swap_indices(programs, i1, i2)


def main():
    inp = get_input(16)
    commands = parse_input(inp)
    programs = list(string.ascii_lowercase[:16])

    for c, *args in commands:
        if c == 's':
            spin_programs(programs, *args)
        elif c == 'p':
            swap_names(programs, *args)
        elif c == 'x':
            swap_indices(programs, *args)
    print('Task 1:', ''.join(programs))



if __name__ == "__main__":
    main()
