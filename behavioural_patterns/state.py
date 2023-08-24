from abc import ABC, abstractmethod

# State interface
class State(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete State classes
class PlayingState(State):
    def play(self):
        print("Already playing")

    def pause(self):
        print("Paused")
        return PausedState()

    def stop(self):
        print("Stopped")
        return StoppedState()

class PausedState(State):
    def play(self):
        print("Resumed playing")
        return PlayingState()

    def pause(self):
        print("Already paused")

    def stop(self):
        print("Stopped")
        return StoppedState()

class StoppedState(State):
    def play(self):
        print("Started playing")
        return PlayingState()

    def pause(self):
        print("Cannot pause, already stopped")

    def stop(self):
        print("Already stopped")

# Context class
class AudioPlayer:
    def __init__(self):
        self.state = StoppedState()

    def change_state(self, state):
        self.state = state

    def play(self):
        self.state = self.state.play()

    def pause(self):
        self.state = self.state.pause()

    def stop(self):
        self.state = self.state.stop()

# Using the AudioPlayer
player = AudioPlayer()

player.play()   # Output: Started playing
player.pause()  # Output: Paused
player.play()   # Output: Resumed playing
player.stop()   # Output: Stopped
player.pause()  # Output: Cannot pause, already stopped
