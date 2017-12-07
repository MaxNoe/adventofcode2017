from . import get_input
import re

tower_re = re.compile('^([a-z]{4}) [(]([0-9]+)[)](?: -> ([a-z, ]+))?$')


def parse_input(inp):
    groups = map(lambda s: tower_re.match(s).groups(), inp.splitlines())
    return [
        (c[0], int(c[1]), c[2].split(', ') if c[2] else [])
        for c in groups
    ]



def main():
    my_input = get_input(7)




if __name__ == '__main__':
    main()

