# Observer interface (Step 1): The Observer class defines the update method, which concrete observers must implement.

# Concrete Observer classes (Step 2): The User class is a concrete observer that implements the update method to react to changes.

# Subject class (Step 3): The Subject class maintains a list of observers and provides methods to manage them.

# Concrete Subject class (Step 4): The MessageSystem class is a concrete subject that inherits from Subject. It holds the state (message) and triggers notifications to observers.

# Usage: In the usage section, we create instances of concrete subjects and observers. We attach observers to the subject and let the subject notify observers of changes.

from abc import ABC, abstractmethod


# Step 1: Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


# Step 2: Concrete Observer classes
class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received a new message: {message}")


# Step 3: Subject class
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


# Step 4: Concrete Subject class
class MessageSystem(Subject):
    def send_message(self, message):
        print(f"Sending message: {message}")
        self.notify(message)


# Usage
message_system = MessageSystem()

user1 = User("Alice")
user2 = User("Bob")
user3 = User("Charlie")

message_system.attach(user1)
message_system.attach(user2)
message_system.attach(user3)

message_system.send_message("Hello, everyone!")
# Alice received a new message: Hello, everyone!
# Bob received a new message: Hello, everyone!
# Charlie received a new message: Hello, everyone!
