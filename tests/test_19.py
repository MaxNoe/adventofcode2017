with open('tests/inp19.txt') as f:
    inp = f.read()


def test_letters():
    from adventofcode2017.day19 import find_letters

    assert find_letters(inp.splitlines()) == 'ABCDEF'


def test_find_entry():
    from adventofcode2017.day19 import find_entry
    diagram = inp.splitlines()
    entry = find_entry(diagram)
    assert entry == (0, 5)


def test_path():
    from adventofcode2017.day19 import next_step, find_entry

    diagram = inp.splitlines()
    entry = find_entry(diagram)
    assert entry == (0, 5)

    pos, direction = next_step(diagram, entry)
    assert pos == (1, 5)

    pos, direction = next_step(diagram, pos, direction)
    assert pos == (2, 5)

    pos, direction = next_step(diagram, pos, direction)
    assert pos == (3, 5)

    pos, direction = next_step(diagram, pos, direction)
    assert pos == (4, 5)

    pos, direction = next_step(diagram, pos, direction)
    assert pos == (5, 5)

    pos, direction = next_step(diagram, pos, direction)
    assert pos == (5, 6)

    pos, direction = next_step(diagram, pos, direction)
    assert pos == (5, 7)

    pos, direction = next_step(diagram, pos, direction)
    assert pos == (5, 8)

    pos, direction = next_step(diagram, pos, direction)
    assert pos == (4, 8)

