"""
Vector class with unit tests
"""
import math
import unittest


class Vector:
    """
    Vector class with x and y coordinates
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __bool__(self):
        return bool(abs(self))


class TestVector(unittest.TestCase):
    def test_print_vector(self):
        exp = 'Vector(1, 5)'
        self.assertEqual(str(Vector(1, 5)), exp)
