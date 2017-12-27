from . import get_input


def parse_input(inp):
    infected = set()
    center = len(inp.splitlines()) // 2
    for i, row in enumerate(inp.splitlines()):
        for j, node in enumerate(row):
            if node == '#':
                infected.add((j - center, center - i))
    return infected


def do_burst(position, direction, infected):
    if position in infected:
        direction = direction[1], -direction[0]
        new_infection = False
        infected.remove(position)
    else:
        direction = -direction[1], direction[0]
        new_infection = True
        infected.add(position)

    position = position[0] + direction[0], position[1] + direction[1]

    return position, direction, new_infection

def main():
    inp = get_input(22)
    infected = parse_input(inp)

    position = (0, 0)
    direction = (0, 1)
    new_infections = 0
    for i in range(10000):
        position, direction, new_infection = do_burst(position, direction, infected)
        new_infections += new_infection

    print('Task 1:', new_infections)


if __name__ == "__main__":
    main()

