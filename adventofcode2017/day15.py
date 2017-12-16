from . import get_input


def generator(f, seed):
    value = seed
    while True:
        value = (value * f) % 2147483647
        yield value


def compare(a, b):
    # compare the lowest 16 bits
    return ((a << 16) & 0xffffffff) == ((b << 16) & 0xffffffff)


def judge(seed_a, seed_b, steps):
    n = 0
    gen_a = generator(16807, seed_a)
    gen_b = generator(48271, seed_b)
    for _ in range(steps):
        a = next(gen_a)
        b = next(gen_b)
        n += compare(a, b)
    return n


def main():
    inp = get_input(15)
    lines = inp.splitlines()

    seed_a = int(lines[0].split()[-1])
    seed_b = int(lines[1].split()[-1])

    print('Task 1:', judge(seed_a, seed_b, int(40e6)))


if __name__ == "__main__":
    main()
