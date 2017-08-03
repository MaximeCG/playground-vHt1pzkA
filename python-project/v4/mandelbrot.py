from math import log2

MAX_ITER = 100

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) < 2:
        if n == MAX_ITER:
            return MAX_ITER
        z = z*z + c
        n += 1

    return n + 1 - log2(log2(abs(z)))
