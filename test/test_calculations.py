import sys
import os
import numpy as np

# Add the base directory to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from calculations import (
    add,
    sub,
    mult,
    div,
    sqrt,
)

a = 1.4
b = 0.1


def test_add():
    assert add(a, b) == a + b


def test_sub():
    assert sub(a, b) == a - b


def test_mult():
    assert mult(a, b) == a * b


def test_div():
    assert div(a, b) == a / b


def test_sqrt():
    assert sqrt(a) == np.sqrt(a)


# Adding additional tests with numpy
a_arr = np.random.normal(0, 1, 100)
b_arr = np.random.normal(0, 1, 100)


def test_arrays():
    assert np.all(add(a_arr, b_arr) == a_arr + b_arr)
    assert np.all(sub(a_arr, b_arr) == a_arr - b_arr)
    assert np.all(mult(a_arr, b_arr) == a_arr * b_arr)
    assert np.all(div(a_arr, b_arr) == a_arr / b_arr)
    assert np.all(
        sqrt(a_arr) == np.array([np.sqrt(_a) if _a > 0 else 0 for _a in a_arr])
    )
