from . import get_input


from .day15_ext import judge, next_value


def generator(f, seed):
    value = seed
    while True:
        value = next_value(value, f)
        yield value


def main():
    inp = get_input(15)
    lines = inp.splitlines()

    seed_a = int(lines[0].split()[-1])
    seed_b = int(lines[1].split()[-1])

    print('Task 1:', judge(seed_a, seed_b, int(40e6)))


if __name__ == "__main__":
    main()
