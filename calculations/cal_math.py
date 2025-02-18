from numpy import sqrt as np_sqrt


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def sqrt(a):
    if a > 0:
        return np_sqrt(a)
    return 0
