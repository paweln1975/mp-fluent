import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


if __name__ == "__main__":
    import doctest

    doctest.testfile('tests/vector2d.doctest', verbose=True)
