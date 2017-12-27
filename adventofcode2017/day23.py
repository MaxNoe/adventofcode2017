from . import get_input
from .day18 import parse_input
import math


def main():
    instructions = parse_input(get_input(23))

    print('Task 1:', count_mul(instructions))
    print('Task 2:', check_prime(instructions))


def check_prime(instructions):

    registers = {k: 0 for k in 'abcdefgh'}
    registers['a'] = 1

    pos = 0
    for i in range(50):
        instruction, args = instructions[pos]
        args = args.copy()

        if len(args) > 1 and isinstance(args[1], str):
            args[1] = registers[args[1]]

        if instruction == 'set':
            registers[args[0]] = args[1]
        elif instruction == 'sub':
            registers[args[0]] -= args[1]
        elif instruction == 'mul':
            registers[args[0]] *= args[1]

        if isinstance(args[0], str):
            args[0] = registers[args[0]]

        if instruction == 'jnz' and args[0] != 0:
            pos += args[1]
        else:
            pos += 1

    non_primes = 0
    for i in range(registers['b'], registers['c'] + 1, 17):
        if not is_prime(i):
            non_primes += 1
    return non_primes


def is_prime(n):
    if n % 2 == 0:
        return False

    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True


def count_mul(instructions):
    pos = 0
    n_mul = 0
    registers = {k: 0 for k in 'abcdefgh'}

    while 0 <= pos < len(instructions):
        instruction, args = instructions[pos]
        args = args.copy()

        if len(args) > 1 and isinstance(args[1], str):
            args[1] = registers[args[1]]

        if instruction == 'set':
            registers[args[0]] = args[1]
        elif instruction == 'sub':
            registers[args[0]] -= args[1]
        elif instruction == 'mul':
            registers[args[0]] *= args[1]
            n_mul += 1

        if isinstance(args[0], str):
            args[0] = registers[args[0]]

        if instruction == 'jnz' and args[0] != 0:
            pos += args[1]
        else:
            pos += 1

    return n_mul


if __name__ == "__main__":
    main()
