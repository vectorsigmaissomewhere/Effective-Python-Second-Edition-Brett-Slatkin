print("Program number 1")
def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) -> {result!r}')
        return result
    return wrapper

@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(4)
"""
fibonacci((1,), {}) -> 1
fibonacci((0,), {}) -> 0
fibonacci((2,), {}) -> 1
fibonacci((1,), {}) -> 1
fibonacci((3,), {}) -> 2
fibonacci((1,), {}) -> 1
fibonacci((0,), {}) -> 0
fibonacci((2,), {}) -> 1
fibonacci((4,), {}) -> 3
"""

print(fibonacci)
# <function trace.<locals>.wrapper at 0x7cc1915887c0>


print("Program number 2")
import pickle
from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) -> {result!r}')
        return result
    return wrapper

@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

help(fibonacci)

print(pickle.dumps(fibonacci))
