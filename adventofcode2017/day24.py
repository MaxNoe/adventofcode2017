from . import get_input


def main():
    components = parse_input(get_input(24))

    bridges = build_bridges(components)
    best_bridge = find_best_bridge(bridges)
    print('Task 1:', calc_strength(best_bridge))

    longest_bridge = find_longest_bridge(bridges)
    print('Task 2:', calc_strength(longest_bridge))


def parse_input(inp):
    return list(map(
        lambda s: tuple(map(int, s.split('/'))),
        inp.splitlines()
    ))


def calc_strength(bridge):
    return sum(map(sum, bridge))


def find_longest_bridge(bridges):
    return sorted(bridges, key=lambda b: (len(b), calc_strength(b)))[-1]


def build_bridges(components, open_connection=0):
    bridges = []
    orig_open = open_connection

    for component in components:
        open_connection = orig_open
        if open_connection in component:
            open_connection = component[not component.index(open_connection)]
            bridge = [component]
            bridges.append(bridge)

            new_comps = components[:]
            new_comps.remove(component)
            subcomps = build_bridges(new_comps, open_connection)
            for subcomp in subcomps:
                bridges.append(bridge + subcomp)
    return bridges


def find_best_bridge(bridges):
    return sorted(bridges, key=calc_strength)[-1]


if __name__ == "__main__":
    main()
