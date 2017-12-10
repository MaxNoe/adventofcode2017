from . import get_input


def parse_input(inp):
    return list(map(int, inp.split(',')))


def do_twist(elements, index, length, skip_size):
    start = index
    end = index + length
    n_wrapped = end - len(elements)

    selected = elements[start:end]
    if n_wrapped > 0:
        selected.extend(elements[:n_wrapped])

    selected.reverse()

    for i in range(length):
        idx = (index + i) % len(elements)
        elements[idx] = selected[i]

    index = (index + skip_size + length) % len(elements)
    skip_size += 1

    return index, skip_size


def main():
    inp = get_input(10)
    lengths = parse_input(inp)
    skip_size = 0
    index = 0
    elements = list(range(256))

    for length in lengths:
        index, skip_size = do_twist(elements, index, length, skip_size)

    print('Task 1', elements[0] * elements[1])



if __name__ == '__main__':
    main()
