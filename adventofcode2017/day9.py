from . import get_input


def calc_score(inp):
    level = 0
    score = 0

    garbage = False
    ignore = False

    for c in inp:
        if not garbage:
            if c == '<':
                garbage = True

            elif c == '{':
                level += 1

            elif c == '}':
                score += level
                level -= 1

        else:
            if ignore is True:
                ignore = False
                continue

            if c == '!':
                ignore = True

            if c == '>':
                garbage = False
    return score


def main():
    inp = get_input(9)

    print('Task 1:', calc_score(inp))


if __name__ == '__main__':
    main()
