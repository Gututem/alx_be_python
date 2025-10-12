import math

class Shape:
    """Base class representing a generic geometric shape."""

    def area(self):
        """Raise error to enforce overriding in derived classes."""
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    """Derived class representing a rectangle."""

    def __init__(self, length, width):
        """Initialize rectangle dimensions."""
        self.length = length
        self.width = width

    def area(self):
        """Override area method to calculate rectangle area."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""

    def __init__(self, radius):
        """Initialize circle radius."""
        self.radius = radius

    def area(self):
        """Override area method to calculate circle area."""
        return math.pi * (self.radius ** 2)
