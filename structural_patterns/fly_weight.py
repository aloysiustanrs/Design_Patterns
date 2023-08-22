# The Flyweight design pattern is a structural pattern that focuses on minimizing memory usage by sharing as much data as possible between similar objects

# optimize memory usage by reusing objects when their internal state can be shared , eg : color & radius (stored internally)

# extrinsic (context-specific) state of objects can be provided through constructor when created
import random


class Circle:
    def __init__(self, color):
        self.color = color
        self.radius = 10  # Shared intrinsic state

    def draw(self, x, y):
        print(f"Drawing a {self.color} circle at ({x}, {y}) with radius {self.radius}")


class CircleFactory:
    _circle_pool = {}

    @staticmethod
    def get_circle(color):
        if color not in CircleFactory._circle_pool:
            CircleFactory._circle_pool[color] = Circle(color)
        return CircleFactory._circle_pool[color]


# Client code
colors = ["Red", "Green", "Blue", "Yellow", "Pink"]
factory = CircleFactory()

for _ in range(20):
    color = random.choice(colors)
    circle = factory.get_circle(color)
    circle.draw(random.randint(0, 100), random.randint(0, 100))
