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


def do_burst_mutated(position, direction, states):
    state = states.get(position, 'clean')

    if state == 'clean':
        direction = -direction[1], direction[0]
        states[position] = 'weakened'
        new = 0
    elif state == 'weakened':
        new = 1
        states[position] = 'infected'
    elif state == 'infected':
        direction = direction[1], -direction[0]
        states[position] = 'flagged'
        new = 0
    elif state == 'flagged':
        direction = -direction[0], -direction[1]
        states[position] = 'clean'
        new = 0

    position = position[0] + direction[0], position[1] + direction[1]

    return position, direction, new


def puzzle_1(inp):
    infected = parse_input(inp)

    position = (0, 0)
    direction = (0, 1)
    new_infections = 0
    for i in range(10000):
        position, direction, new_infection = do_burst(position, direction, infected)
        new_infections += new_infection
    return new_infections


def puzzle_2(inp):
    infected = parse_input(inp)
    states = {p: 'infected' for p in infected}

    position = (0, 0)
    direction = (0, 1)
    new_infections = 0
    for i in range(10000000):
        position, direction, new_infection = do_burst_mutated(position, direction, states)
        new_infections += new_infection
    return new_infections


def main():
    inp = get_input(22)

    print('Task 1:', puzzle_1(inp))
    print('Task 2:', puzzle_2(inp))


if __name__ == "__main__":
    main()

