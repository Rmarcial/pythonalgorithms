"""
Class Fraction, to emulate fractional numbers
"""


class Fraction(object):
    """
    Number represented as a fraction
    """

    def __init__(self, num, den):
        """ num and den are integers """
        assert type(num) == int and type(den) == int

        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        n = other.den * self.num + self.den * other.num
        d = self.den * other.den
        return Fraction(n, d)

    def __float__(self):
        return self.num / self.den


# tests
f1 = Fraction(3, 4)
f2 = Fraction(5, 7)

print(f1)
print(f2)
f3 = f1 + f2
print(f3)
print(float(f1))
print(float(f2))
