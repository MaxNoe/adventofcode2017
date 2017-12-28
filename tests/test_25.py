inp = '''Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
'''

expected = dict(
    initial_state='A',
    steps=6,
    states={
        'A': [
            [
                ('write', 1),
                ('move', 1),
                ('continue', 'B'),
            ],
            [
                ('write', 0),
                ('move', -1),
                ('continue', 'B'),
            ]
        ],
        'B': [
            [
                ('write', 1),
                ('move', -1),
                ('continue', 'A'),
            ],
            [
                ('write', 1),
                ('move', 1),
                ('continue', 'A'),
            ]
        ],
    }
)


def test_parse():
    from adventofcode2017.day25 import parse_input

    assert parse_input(inp) == expected


def test_calc_checksum():
    from adventofcode2017.day25 import calc_checksum
    assert calc_checksum(expected) == 3
