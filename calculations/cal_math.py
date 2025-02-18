from numpy import sqrt as np_sqrt
from numpy import vectorize


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


@vectorize
def sqrt(a):
    if a > 0.0:
        return np_sqrt(a)
    return 0.0
