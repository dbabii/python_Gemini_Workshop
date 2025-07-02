class Polygon:
    """
    This is a parent class of shapes
    """
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    @property
    def num_sides(self):
        return len(self.side_lengths)

    @property
    def perimeter(self):
        return sum(self.side_lengths)

    def __str__(self):
        return 'Polygon with %s sides' % self.side_lengths


class Rectangle(Polygon):
    def __init__(self, height, weight):
        super().__init__([height, weight, height, weight])

    @property
    def area(self):
        return self.side_lengths[0] * self.side_lengths[1]

class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)


shape1 = Rectangle(5, 6)
print(shape1.area)
print(shape1.perimeter)

s = Square(5)
print(s.area)
print(s.perimeter)