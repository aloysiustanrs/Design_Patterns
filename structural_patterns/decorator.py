# Decorator is a structural pattern that allows adding new behaviors to objects dynamically by placing them inside special wrapper objects, called decorators.

# Basically a wrapper that wraps a object and does something without affecting the object's code


class Coffee:
    def cost(self):
        return 5  # Basic cost of coffee


class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 3  # Additional cost for milk


class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1  # Additional cost for sugar


# Create a basic coffee
basic_coffee = Coffee()
print("Cost of basic coffee:", basic_coffee.cost())

# Add milk to the coffee
coffee_with_milk = MilkDecorator(basic_coffee)
print("Cost of coffee with milk:", coffee_with_milk.cost())

# Add sugar to the coffee
coffee_with_sugar = SugarDecorator(basic_coffee)
print("Cost of coffee with sugar:", coffee_with_sugar.cost())

# Add both milk and sugar to the coffee
coffee_with_milk_and_sugar = SugarDecorator(MilkDecorator(basic_coffee))
print("Cost of coffee with milk and sugar:", coffee_with_milk_and_sugar.cost())
