inp = '''set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
'''

instructions = [
    ('set', ['a', 1]),
    ('add', ['a', 2]),
    ('mul', ['a', 'a']),
    ('mod', ['a', 5]),
    ('snd', ['a']),
    ('set', ['a', 0]),
    ('rcv', ['a']),
    ('jgz', ['a', -1]),
    ('set', ['a', 1]),
    ('jgz', ['a', -2]),
]


def test_parse_input():
    from adventofcode2017.day18 import parse_input
    assert instructions == parse_input(inp)


def test_recover():
    from adventofcode2017.day18 import get_first_recovered_freq
    assert get_first_recovered_freq(instructions) == 4
