from itertools import zip_longest

from . import get_input


def solve_captcha(numbers):

    s = 0
    for n0, n1 in zip_longest(numbers, numbers[1:], fillvalue=numbers[0]):
        if n0 == n1:
            s += n0
    return s


def main():
    my_input = get_input(1)

    numbers = list(map(int, my_input.strip()))

    print('Task 1:', solve_captcha(numbers))



if __name__ == '__main__':
    main()
