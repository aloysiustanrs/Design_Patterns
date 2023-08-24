from abc import ABC, abstractmethod

# Abstract class with template methods
class BeverageTemplate(ABC):
    def prepare_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

# Concrete subclasses
class Coffee(BeverageTemplate):
    def brew(self):
        print("Brewing coffee grounds")

    def add_condiments(self):
        print("Adding sugar and milk")

class Tea(BeverageTemplate):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

# Using the template methods
def make_beverage(beverage):
    print(f"Making {beverage.__class__.__name__}")
    beverage.prepare_beverage()
    print()

coffee = Coffee()
tea = Tea()

make_beverage(coffee)
make_beverage(tea)
