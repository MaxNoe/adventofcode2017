from itertools import zip_longest

from . import get_input


def solve_captcha(numbers):

    s = 0
    for n0, n1 in zip_longest(numbers, numbers[1:], fillvalue=numbers[0]):
        if n0 == n1:
            s += n0
    return s


def solve_captcha_2(numbers):

    l = len(numbers)
    double = numbers + numbers

    s = 0
    for i, n in enumerate(numbers):
        if n == double[l // 2 + i]:
            s += n
    return s


def main():
    my_input = get_input(1)

    numbers = list(map(int, my_input.strip()))

    print('Task 1:', solve_captcha(numbers))
    print('Task 2:', solve_captcha_2(numbers))



if __name__ == '__main__':
    main()
