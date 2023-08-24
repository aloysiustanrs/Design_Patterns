from abc import ABC, abstractmethod

# Strategy interface
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

# Concrete Strategy classes
class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price

class TenPercentDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.9

class TwentyPercentDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.8

# Context class
class ShoppingCart:
    def __init__(self, discount_strategy):
        self.items = []
        self.discount_strategy = discount_strategy

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return self.discount_strategy.apply_discount(total)

# Using the ShoppingCart
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

item1 = Item("Item 1", 100)
item2 = Item("Item 2", 200)

cart_no_discount = ShoppingCart(NoDiscount())
cart_10_percent_discount = ShoppingCart(TenPercentDiscount())
cart_20_percent_discount = ShoppingCart(TwentyPercentDiscount())

cart_no_discount.add_item(item1)
cart_no_discount.add_item(item2)

cart_10_percent_discount.add_item(item1)
cart_10_percent_discount.add_item(item2)

cart_20_percent_discount.add_item(item1)
cart_20_percent_discount.add_item(item2)

print("Total (No Discount):", cart_no_discount.calculate_total())
print("Total (10% Discount):", cart_10_percent_discount.calculate_total())
print("Total (20% Discount):", cart_20_percent_discount.calculate_total())
