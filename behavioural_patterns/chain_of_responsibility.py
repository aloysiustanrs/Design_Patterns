# The Chain of Responsibility is a behavioral design pattern that allows an object to pass a request along a chain of potential handlers until the request is handled or the end of the chain is reached.
# Each handler in the chain has the ability to either handle the request or pass it along to the next handler in the chain.


class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        pass


class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request == "handler1":
            print("ConcreteHandler1 handled the request.")
        elif self._successor:
            self._successor.handle_request(request)


class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request == "handler2":
            print("ConcreteHandler2 handled the request.")
        elif self._successor:
            self._successor.handle_request(request)


class ConcreteHandler3(Handler):
    def handle_request(self, request):
        if request == "handler3":
            print("ConcreteHandler3 handled the request.")
        elif self._successor:
            self._successor.handle_request(request)


# Creating the chain of handlers
handler1 = ConcreteHandler1()
handler2 = ConcreteHandler2()
handler3 = ConcreteHandler3()

handler1._successor = handler2
handler2._successor = handler3

# Sending requests through the chain
handler1.handle_request("handler2")  # ConcreteHandler2 handled the request.
handler1.handle_request("handler3")  # ConcreteHandler3 handled the request.
handler1.handle_request("handler1")  # ConcreteHandler1 handled the request.
handler1.handle_request("unknown")  # Request not handled by any handler.
