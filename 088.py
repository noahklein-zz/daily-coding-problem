"""
Implement division of two positive integers without using the division,
multiplication, or modulus operators. Return the quotient as an integer,
ignoring the remainder.

"""


def divides(a, b):
    if b == 0:
        raise ArithmeticError()
    if a < b:
        return 0
    return 1 + divides(a - b, b)


assert(divides(10, 1) == 10)
assert(divides(0, 100) == 0)
assert(divides(17, 4) == 4)
assert(divides(100, 5) == 20)
