"""lista 4 zad4 Wojciech Wroblewski"""
from inspect import getfullargspec
import math

function_store = {}


class Method(object):
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        func = Method(self.function)
        function = function_store.get(func.characteristic_value(args))
        return function(*args, **kwargs)

    """ dodanie funkcji do slownika"""

    def register_in_list(self, function):
        func = Method(function)
        function_store[func.characteristic_value()] = function
        return func

    """ zwraca dane charakterystyczne dla funkcji"""

    def characteristic_value(self, args=None):
        if args is None:
            args = getfullargspec(self.function).args

        return tuple([
            self.function.__class__,
            self.function.__name__,
            len(args),
        ])


def overload(function):
    func = Method(function)
    return func.register_in_list(function)


@overload
def norm(x, y):
    return math.sqrt(x * x + y * y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


print(f"norm(2,4) = {norm(2, 4)}")

print(f"norm(2,3,4) = {norm(2, 3, 4)}")
