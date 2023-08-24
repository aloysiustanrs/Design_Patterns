# Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request.
# This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.


# Command is the abstract interface with the execute method.
# LightOnCommand and LightOffCommand are concrete command classes that encapsulate actions of turning the light on and off, respectively.
# Light is the receiver that performs the actual operations.
# RemoteControl is the invoker that holds and triggers commands.
# The client creates the commands and sets them in the invoker to control the receiver's actions.


from abc import ABC, abstractmethod


# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Concrete command classes
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# Receiver
class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")


# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()


# Client code
light = Light()

light_on_command = LightOnCommand(light)
light_off_command = LightOffCommand(light)

remote = RemoteControl()

remote.set_command(light_on_command)
remote.press_button()  # Output: Light is on

remote.set_command(light_off_command)
remote.press_button()  # Output: Light is off
