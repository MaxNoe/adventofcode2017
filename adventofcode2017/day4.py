from . import get_input

from functools import partial


def is_valid_password(password, anagrams=True):

    words = password.split()

    if anagrams is True:
        unique_words = set(words)
    else:
        unique_words = set(map(tuple, map(sorted, words)))

    return len(unique_words) == len(words)


def main():
    my_input = get_input(4)

    passwords = my_input.splitlines()
    n_valid = sum(map(is_valid_password, passwords))

    print('Task 1:', n_valid)

    is_valid_no_anagrams = partial(is_valid_password, anagrams=False)
    n_valid_no_anagrams = sum(map(is_valid_no_anagrams, passwords))
    print('Task 2:', n_valid_no_anagrams)


if __name__ == '__main__':
    main()
