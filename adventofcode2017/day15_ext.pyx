cpdef int next_value(int value, int f):
    cdef int m = 2147483647
    return (<long>value * f) % m


cdef int compare(int a, int b):
    return (a << 16) == (b << 16)


def judge(int a, int b, int steps):
    cdef int n = 0

    cdef int i
    for i in range(steps):
        a = next_value(a, 16807)
        b = next_value(b, 48271)

        n += compare(a, b)

    return n

