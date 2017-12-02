my_input = '''5	9	2	8
9	4	7	3
3	8	6	5
'''.strip()

spreadsheet = [
    [5, 9, 2, 8],
    [9, 4, 7, 3],
    [3, 8, 6, 5],
]


def test_1():
    from adventofcode2017.day2 import parse_spreadsheet

    assert parse_spreadsheet(my_input) == spreadsheet


def test_2():
    from adventofcode2017.day2 import calc_row_checksum_division

    assert calc_row_checksum_division(spreadsheet[0]) == 4
    assert calc_row_checksum_division(spreadsheet[1]) == 3
    assert calc_row_checksum_division(spreadsheet[2]) == 2


def test_3():
    from adventofcode2017.day2 import calc_row_checksum_division, calc_checksum

    assert calc_checksum(spreadsheet, calc_row_checksum_division) == 9
