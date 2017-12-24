import string

from . import get_input

DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))


def find_entry(diagram):
    return 0, diagram[0].index('|')


def next_step(diagram, pos, direction=(1, 0)):
    r, c = pos
    dr, dc = direction

    if diagram[r + dr][c + dc] != ' ':
        return (r + dr, c + dc), direction

    for dr, dc in DIRECTIONS:
        if diagram[r + dr][c + dc] != ' ' and (-dr, -dc) != direction:
            return (r + dr, c + dc), (dr, dc)

    return pos, None


def find_letters(diagram):
    pos = find_entry(diagram)

    pos, direction = next_step(diagram, pos)

    letters = ''
    while direction is not None:
        pos, direction = next_step(diagram, pos, direction)
        if diagram[pos[0]][pos[1]] in string.ascii_uppercase:
            letters += diagram[pos[0]][pos[1]]
    return letters[:-1]


def main():
    inp = get_input(19)
    diagram = inp.splitlines()
    print('Task 1:', find_letters(diagram))


if __name__ == "__main__":
    main()
