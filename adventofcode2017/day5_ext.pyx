from cpython cimport bool

def do_step(int position, instructions):
    cdef int steps = instructions[position]

    instructions[position] += 1
    position += steps

    return position, instructions


def do_step_2(int position, instructions):
    cdef int steps = instructions[position]


    if steps < 3:
        instructions[position] += 1
    else:
        instructions[position] -= 1
    position += steps

    return position, instructions


def count_steps(instructions, puzzle2=False):
    instructions = instructions.copy()

    cdef int position = 0
    cdef int steps = 0
    cdef int n_instructions = len(instructions)

    while position < n_instructions:
        if not puzzle2:
            position, instructions = do_step(position, instructions)
        else:
            position, instructions = do_step_2(position, instructions)
        steps += 1
    return steps

