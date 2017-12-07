from cpython cimport bool
from cpython cimport array
import array

cdef do_step(int position, int[:] instructions):
    cdef int steps = instructions[position]

    instructions[position] += 1
    position += steps

    return position


cdef do_step_2(int position, int[:] instructions):
    cdef int steps = instructions[position]


    if steps < 3:
        instructions[position] += 1
    else:
        instructions[position] -= 1
    position += steps

    return position


def count_steps(instructions, bool puzzle2=False):
    instructions = instructions.copy()

    cdef int position = 0
    cdef int steps = 0
    cdef int n_instructions = len(instructions)
    cdef int[:] instruction_array = array.array('i', instructions)

    while position < n_instructions:
        if not puzzle2:
            position = do_step(position, instruction_array)
        else:
            position = do_step_2(position, instruction_array)
        steps += 1
    return steps

