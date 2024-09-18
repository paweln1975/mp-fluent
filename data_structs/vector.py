"""
Vector class with doc tests
"""
import math


class Vector:
    """
    Vector class with x and y coordinates
    >>> v = Vector(2, 4)
    >>> v
    Vector(2, 4)
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        >>> v1 = Vector(2, 1)
        >>> v2 = Vector(5, -1)
        >>> v3 = v1 + v2
        >>> v3
        Vector(7, 0)
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """
        Scalar multiplication::
        >>> v = Vector(3, 4)
        >>> v * 3
        Vector(9, 12)
        >>> abs(v * 3)
        15.0
        """
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        """
        Absolute value
        >>> v = Vector(3, 4)
        >>> abs(v)
        5.0
        """
        return math.hypot(self.x, self.y)

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __bool__(self):
        """
        Boolean value
        >>> v = Vector(4, 5)
        >>> bool(v)
        True

        >>> v = Vector(0, 0)
        >>> bool(v)
        False
        """
        return bool(abs(self))

