print("Example no 1")
# dividing a number by 0 returning none
def careful_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

print(careful_divide(2,0))
"""
None
"""


print("Example no 2")
# same code but in different way 
x, y = 1, 0
result = careful_divide(x,y)
if result is None:
    print('Invaild inputs')
"""
Invalid inputs
"""


print("Example no 3")
# The same code but in different way 
# splits the value in tuple
def careful_divide(a, b):
    try:
        return True, a/b
    except ZeroDivisionError:
        return False, None
print(careful_divide(1, 0))
"""
(False,None)
"""

print("Example no 4")
# The same code but in different way 
success, result = careful_divide(x, y)
if not success:
    print('Invalid inputs')
careful_divide(1,0)
"""
Invalid inputs
"""


print("Example no 5")
# you can use underscore variable 
# for unused variables
# which can lead to error

_, result = careful_divide(x, y)
if not result:
    print('Invalid inputs')
careful_divide(1,0)

"""
Invalid inputs
"""

print("Example no 6")
def careful_divide(a,b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invlid inputs')
print(careful_divide(1,1))
"""
Throws the exception
"""

print("Example no 7")
x, y = 5, 2
try:
    result = careful_divide(x,y)
except ValueError:
    print('Result is %.1f' % result)


"""
ZeroDivisionError: division by zero if y is 0 
"""

print("Example no 8")
x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)

"""
Result is 2.5
"""

print("Example no 9")
# functions with type annotations and docstrings
def careful_divide(a : float, b : float) -> float:
    """Divides a by b.
    Raises:
        ValueError: when the inputs cannot be divided
    """
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')
    
print(careful_divide(1,1))
"""
1.0 when a and b is 1
ZeroDivisionError: division by zero when a is any number and b is 0
"""

#  IMPORTANT THINGS TO REMEMBER
"""
functions that return None are error prone 
because None and other value example 0 or empty string 
in conditional expressions evaluate to False
"""

"""
raise exceptions to indicate special situations 
instead of returning None
"""

"""
exception part of function interface 
known as checked exceptions
"""

"""
Type annotations can be used to make it clear 
that a function will never return the value None, 
even in special situaltions
"""
