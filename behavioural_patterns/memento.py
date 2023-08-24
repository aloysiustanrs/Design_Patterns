# Memento: The memento is an object that holds the state of the originator at a specific point in time. It provides methods to access the saved state but doesn't expose the internal details of the originator.
class Memento:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content


# Originator: This is the object whose state needs to be saved and restored. It creates and uses mementos to save its internal state.
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text):
        self._content += text

    def get_content(self):
        return self._content

    def save(self):
        return Memento(self._content)

    def restore(self, memento):
        self._content = memento.get_content()


# Caretaker: The caretaker is responsible for keeping track of and managing the mementos. It requests mementos from the originator and passes them back to the originator for restoring state.
class History:
    def __init__(self):
        self._mementos = []

    def push(self, memento):
        self._mementos.append(memento)

    def pop(self):
        if self._mementos:
            return self._mementos.pop()


# Usage
editor = TextEditor()
history = History()

editor.write("Hello, ")
history.push(editor.save())  # Save state

editor.write("world!")
print(editor.get_content())  # Output: Hello, world!

editor.restore(history.pop())  # Restore previous state
print(editor.get_content())  # Output: Hello,
