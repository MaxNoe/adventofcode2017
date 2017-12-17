from . import get_input


def build_ring_buffer(size, steps):
    pos = 0
    buf = [0]
    for i in range(1, size):
        pos = (pos + steps) % len(buf)
        buf.insert(pos + 1, i)
        pos = (pos + 1)
    return buf


def main():
    steps = int(get_input(17))

    buf = build_ring_buffer(2018, steps)
    idx = buf.index(2017) + 1
    print('Task 1:', buf[idx])


if __name__ == "__main__":
    main()
