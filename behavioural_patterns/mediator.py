# Mediator is a behavioral design pattern that lets you reduce chaotic dependencies between objects.
# The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.
class Mediator:
    def send_message(self, message, user):
        pass


class ChatMediator(Mediator):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, user):
        for u in self.users:
            if u != user:
                u.receive(message)


class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message):
        print(f"{self.name} receives: {message}")


# Usage
mediator = ChatMediator()

user1 = User("Alice", mediator)
user2 = User("Bob", mediator)
user3 = User("Charlie", mediator)

mediator.add_user(user1)
mediator.add_user(user2)
mediator.add_user(user3)

user1.send("Hello, everyone!")
user3.send("Hey there!")
