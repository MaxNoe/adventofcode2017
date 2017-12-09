from . import get_input


def calc_score(inp, count_garbage=False):
    level = 0
    score = 0
    garbage_count = 0

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

            elif c == '!':
                ignore = True

            elif c == '>':
                garbage = False
            else:
                garbage_count += 1

    if count_garbage is True:
        return score, garbage_count
    return score


def main():
    inp = get_input(9)

    score, garbage_count = calc_score(inp, True)
    print('Task 1:', score)
    print('Task 2:', garbage_count)


if __name__ == '__main__':
    main()
