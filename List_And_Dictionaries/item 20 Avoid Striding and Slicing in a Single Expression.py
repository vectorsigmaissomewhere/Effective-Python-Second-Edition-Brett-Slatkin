# about stride
"""
========SYNTAX=========
somelist[start:end:stride]

one example is stride makes it easy to group by 
even or odd indexes in a list
"""

# stride means space left by my side in the below example
print("\n 1. Program number 1")
x = ['red','orange','green','blue','purple']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)
"""
output
['red', 'green', 'purple']
['orange', 'blue']
"""

# REVERSING A BYTE STRING IS TO SLICE THE STRING WITH A STRIDE OF -1
print("\n Program number 2")
x = b'mongoose'
y = x[::-1]
print(y)
"""
output
b'esoognom'
"""

# NOTE
"""
This works the same for unicode Strings
"""

# ============FOR EXAMPLE============   
x ='unicodestringofanotherlanguage'
y = x[::-1]
print(y) # this is going to work properly 

# =============DOING THE SAME HWEN DATA IS ENCODED AS A UTF-8 BYTE STRING
w = 'uncodestringofanotherlanguage'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8') # this will give you an error


print("Program number 3")
# Negative strides besides -1 
x = ['a','b','c','d','e','f','g','h']
print(x[::2])
print(x[::-2])
"""
output
['a', 'c', 'e', 'g']
['h', 'f', 'd', 'b']
"""

# ========SOME MORE STRIDES EXAMPLE
x[2::2] # ['c','e','g']
x[-2::-2] # ['g','e','c','a']
x[-2:2:-2] # ['g','e']
x[2:2:-2] #[]


# =============IMPORTANT THING TO REMEMBER WHILE USIN STRIDE
"""
Avoid negative stride value
use positive value , and start , end index and stride value
As using stride becomes more confusing to read
better use only positive stride value without start and end index value

    SOLUTION
prefer using itertools for working with Iterators and Generators which is clearer to read 
If you still want to use stride 
Try to use start and end index value only 
Means don't use all three parameters , using only two parameters if possible 
"""
