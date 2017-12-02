def test_1():
    from adventofcode2017.day2 import calc_row_checksum

    row = [5, 1, 9, 5]

    assert calc_row_checksum(row) == 8

    row = [7, 5, 3]

    assert calc_row_checksum(row) == 4

    row = [2, 4, 6, 8]

    assert calc_row_checksum(row) == 6


def test_2():
    from adventofcode2017.day2 import calc_checksum

    spreadsheet = [
        [5, 1, 9, 5],
        [7, 5, 3],
        [2, 4, 6, 8],
    ]

    assert calc_checksum(spreadsheet) == 18
