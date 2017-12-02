from . import get_input


def calc_row_checksum(row):
    return max(row) - min(row)


def calc_row_checksum_division(row):
    row = sorted(row, reverse=True)
    for i, num in enumerate(row):
        for other in row[i + 1:]:
            if num % other == 0:
                return num / other
    raise ValueError('No even division found')


def calc_checksum(spreadsheet, func=calc_row_checksum):
    return sum(map(func, spreadsheet))


def parse_spreadsheet(text):
    return [
        [int(cell) for cell in row.split()]
        for row in text.splitlines()
    ]


def main():
    my_input = get_input(2)
    spreadsheet = parse_spreadsheet(my_input)

    print('Task 1:', calc_checksum(spreadsheet))
    print('Task 2:', calc_checksum(spreadsheet, calc_row_checksum_division))


if __name__ == '__main__':
    main()
