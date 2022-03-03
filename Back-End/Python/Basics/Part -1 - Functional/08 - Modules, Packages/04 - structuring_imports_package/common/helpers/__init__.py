# helpers

from .calculator import Calc



def say_hello(name):
    return f'Hello {name}'


def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)