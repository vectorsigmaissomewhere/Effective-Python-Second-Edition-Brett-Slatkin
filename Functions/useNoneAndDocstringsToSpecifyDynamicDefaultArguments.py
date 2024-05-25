print("Program number 1")
# print logging messages that are marked with the time of the logged event
# I want the message to include the time when the function was called
# the default value is reevaluated once 

from time import sleep
from datetime import datetime
def log(message, when=datetime.now()):
    print(f'{when}: {message}')

log('Hi there')
sleep(0.1)
log('Hello again')

"""
2024-05-25 11:52:26.990431: Hi there
2024-05-25 11:52:26.990431: Hello again
"""

print("\nProgram number 2")
def log(message, when=None):
    """Log a message with a timestamp.

    Args:
        message: Message to print.
        when: datetime of when the message occured.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f"{when}: {message}")

log("Hi there!")
sleep(0.1)
log("Hello again")

"""
2024-05-25 11:55:31.426441: Hi there!
2024-05-25 11:55:31.527205: Hello again
"""

print("\nProgram number 3")
# load a value encoded as JSON data
# if decoding data fails, I want an empty dictionary to be returned by default:
# here too the default argument values are evaluated only once 
import json
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
"""
Foo: {'stuff': 5, 'meep': 1}
Bar: {'stuff': 5, 'meep': 1}
"""

print("\nProgram number 4")
# to fix this 
# I will make the default value as None
def decode(data, default=None):
    """Load JSON data from a string

    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary 
    """
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default
    
foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
"""
Foo: {'stuff': 5}
Bar: {'meep': 1}
"""

print("\nProgram number 5")
# do this with type annotations
# The argument is marked as having an Optional value that is a datetime
from typing import Optional

def log_typed(message: str, when: Optional[datetime]=None) -> None:
    """Log a message with a timestamp.
    Args:
        message: Message to print.
        when: datetime of when the message occured.
            Defaults to the present time.
    """

    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
"""
Foo: {'stuff': 5}
Bar: {'meep': 1}
"""

# ============CONCLUSION==============
"""
Use None as the default value for any keyword argument has a 
dynamic value. Document the actual default behavior in the function's docstring
"""
