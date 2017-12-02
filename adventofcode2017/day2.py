from . import get_input


def calc_row_checksum(row):
    return max(row) - min(row)


def calc_checksum(spreadsheet):
    return sum(map(calc_row_checksum, spreadsheet))


def parse_spreadsheet(text):
    return [
        [int(cell) for cell in row.split()]
        for row in text.splitlines()
    ]


def main():
    my_input = get_input(2)
    spreadsheet = parse_spreadsheet(my_input)
    print('Task 1:', calc_checksum(spreadsheet))


if __name__ == '__main__':
    main()
