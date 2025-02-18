import sys
import os

# Add the base directory to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from calculations import (
    add,
    sub,
    mult,
    div,
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
