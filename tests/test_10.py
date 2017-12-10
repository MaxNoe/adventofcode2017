inp = '3, 4, 1, 5'
lengths = [3, 4, 1, 5]


def test_parse_input():
    from adventofcode2017.day10 import parse_input

    assert parse_input(inp) == lengths


def test_do_twist():
    from adventofcode2017.day10 import do_twist

    index = 0
    skip_size = 0
    elements = list(range(5))

    index, skip_size = do_twist(elements, index, lengths[0], skip_size)
    assert elements == [2, 1, 0, 3, 4]
    assert index == 3
    assert skip_size == 1

    index, skip_size = do_twist(elements, index, lengths[1], skip_size)
    assert elements == [4, 3, 0, 1, 2]
    assert index == 3
    assert skip_size == 2

    index, skip_size = do_twist(elements, index, lengths[2], skip_size)
    assert elements == [4, 3, 0, 1, 2]
    assert index == 1
    assert skip_size == 3

    index, skip_size = do_twist(elements, index, lengths[3], skip_size)
    assert elements == [3, 4, 2, 1, 0]
    assert index == 4
    assert skip_size == 4


def test_input_2():
    from adventofcode2017.day10 import input_to_lengths

    assert input_to_lengths('1,2,3') == [49, 44, 50, 44, 51]


def test_hash():
    from adventofcode2017.day10 import elf_hash

    assert elf_hash('') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert elf_hash('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert elf_hash('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert elf_hash('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'
