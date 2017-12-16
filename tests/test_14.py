inp = 'flqrgnkx'

result = [
    '##.#.#..',
    '.#.#.#.#',
    '....#.#.',
    '#.#.##.#',
    '.##.#...',
    '##..#..#',
    '.#...#..',
    '##.#.##.',
]


def test_hex2bin():
    from adventofcode2017.day14 import hex2bin
    assert hex2bin('a0c2017') == list(map(int, '10100000110000100000000101110000'))


def test_hash():
    from adventofcode2017.day14 import knothash

    for i in range(8):
        assert knothash(inp, i)[:8] == result[i]


def test_n_used():
    from adventofcode2017.day14 import calc_n_used
    assert calc_n_used(inp) == 8108
