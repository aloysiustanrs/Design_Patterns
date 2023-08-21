# Facade is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.

# Complex 3rd-party subsystem classes
class SubsystemA:
    def operation_a(self):
        return "Subsystem A operation"

class SubsystemB:
    def operation_b(self):
        return "Subsystem B operation"

class SubsystemC:
    def operation_c(self):
        return "Subsystem C operation"

# Facade class simplifying the subsystem interactions
class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()
        self.subsystem_c = SubsystemC()

    def operation(self):
        results = []
        results.append(self.subsystem_a.operation_a())
        results.append(self.subsystem_b.operation_b())
        results.append(self.subsystem_c.operation_c())
        return results

# Client code
def main():
    facade = Facade()
    operations = facade.operation()
    for operation in operations:
        print(operation)

if __name__ == "__main__":
    main()
