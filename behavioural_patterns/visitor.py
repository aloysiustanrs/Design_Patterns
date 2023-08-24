from abc import ABC, abstractmethod

# Visitor interface
class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_square(self, square):
        pass

# Concrete Visitor
class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        return 3.14 * circle.radius ** 2

    def visit_square(self, square):
        return square.side_length ** 2

class PerimeterCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        return 2 * 3.14 * circle.radius

    def visit_square(self, square):
        return 4 * square.side_length

# Element interface
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Concrete Elements
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        return visitor.visit_circle(self)

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def accept(self, visitor):
        return visitor.visit_square(self)

# Using the Visitor pattern
shapes = [Circle(5), Square(4)]

area_calculator = AreaCalculator()
perimeter_calculator = PerimeterCalculator()

for shape in shapes:
    area = shape.accept(area_calculator)
    perimeter = shape.accept(perimeter_calculator)
    print(f"Shape: {shape.__class__.__name__}, Area: {area}, Perimeter: {perimeter}")
