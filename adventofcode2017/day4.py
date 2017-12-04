from . import get_input


def is_valid_password(password):

    words = password.split()
    unique_words = set(words)

    return len(unique_words) == len(words)


def main():
    my_input = get_input(4)

    passwords = my_input.splitlines()
    n_valid = sum(map(is_valid_password, passwords))

    print('Task 1:', n_valid)


if __name__ == '__main__':
    main()
