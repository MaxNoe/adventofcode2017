inp = 'flqrgnkx'

result = list(map(lambda r: list(map(int, r)), '''
##.#.#..
.#.#.#.#
....#.#.
#.#.##.#
.##.#...
##..#..#
.#...#..
##.#.##.
'''.strip().replace('#', '1').replace('.', '0').splitlines()))


def test_hex2bin():
    from adventofcode2017.day14 import hex2bin
    assert hex2bin('a0c2017') == list(map(int, '1010000011000010000000010111'))


def test_hash():
    from adventofcode2017.day14 import knothash

    for i in range(8):
        assert knothash(inp, i)[:8] == result[i]


def test_n_used():
    from adventofcode2017.day14 import calc_n_used, parse_memory
    m = parse_memory(inp)
    assert calc_n_used(m) == 8108


def test_regions():
    from adventofcode2017.day14 import parse_memory, find_regions

    m = parse_memory(inp)

    assert len(find_regions(m)) == 1242
