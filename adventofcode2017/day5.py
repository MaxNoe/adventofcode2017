from . import get_input

from .day5_ext import count_steps, do_step


__all__ = ['count_steps', 'do_step']


def parse_input(inp):
    return list(map(int, inp.split()))



def main():
    my_input = get_input(5)
    instructions = parse_input(my_input)

    print('Puzzle 1: ', count_steps(instructions))
    print('Puzzle 2: ', count_steps(instructions, puzzle2=True))


if __name__ == '__main__':
    main()
