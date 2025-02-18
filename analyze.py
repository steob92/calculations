from calculations import (
    add,
    sub,
    mult,
    div,
)
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

print(f"a = {a}")
print(f"b = {b}")

# Print out the various operations
print(f"a + b = {add(a, b):0.3f}")
print(f"a - b = {sub(a, b):0.3f}")
print(f"a * b = {mult(a, b):0.3f}")
print(f"a / b = {div(a, b):0.3f}")
