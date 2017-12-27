from . import get_input


def parse_input(inp):

    def parse_line(line):
        pattern, result = line.split('=>')
        pattern = tuple(pattern.strip().split('/'))
        result = tuple(result.strip().split('/'))
        return pattern, result

    return dict(map(parse_line, inp.splitlines()))


def rotate(pattern, k):
    k = k % 4
    if k == 0:
        return pattern
    elif k == 1:
        return transpose(fliplr(pattern))
    elif k == 2:
        return fliplr(flipud(pattern))
    else:
        return fliplr(transpose(pattern))


def fliplr(pattern):
    return tuple([r[::-1] for r in pattern])


def flipud(pattern):
    return tuple([r for r in pattern[::-1]])


def transpose(pattern):
    return tuple([
        ''.join(r[i] for r in pattern)
        for i in range(len(pattern))
    ])


def enhance(img, rules):
    result = []
    if len(img) % 2 == 0:
        N = 2
    elif len(img) % 3 == 0:
        N = 3
    else:
        raise ValueError('Must be divisible by 2 or 3')

    for i in range(len(img) // N):
        result.append([])
        for j in range(len(img) // N):
            subimg = tuple([
                img[N * i + row][N * j: N * (j + 1)]
                for row in range(N)
            ])
            result[-1].append(match_pattern(subimg, rules))
    img = []
    for row in result:
        for i in range(N + 1):
            img.append(''.join(subimg[i] for subimg in row))
    return tuple(img)


def match_pattern(subimg, rules):
    for trans in (None, fliplr, flipud):
        if trans is not None:
            subimg = trans(subimg)
        for i in range(4):
            output = rules.get(rotate(subimg, i))
            if output is not None:
                return output

    raise ValueError('Could not find a matching pattern')


def main():
    inp = get_input(21)
    rules = parse_input(inp)
    img = (
        '.#.',
        '..#',
        '###',
    )
    for i in range(5):
        img = enhance(img, rules)

    print('Task 1:', sum(c == '#' for r in img for c in r))

    for i in range(13):
        img = enhance(img, rules)
    print('Task 2:', sum(c == '#' for r in img for c in r))


if __name__ == "__main__":
    main()
