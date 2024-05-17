print("Program number 1")
# sort number and prioritizing a group of number
# this pattern can be useful
def sort_priority(values,group):
    def helper(x):
        if x in group:
            return (0,x)
        return (1,x)
    values.sort(key=helper)

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
sort_priority(numbers,group)
print(numbers)
"""
[2, 3, 5, 7, 1, 4, 6, 8]
"""

print("\n Program number 2")
# Found should be True but you get false
def sortpriority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found
numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
found = sortpriority2(numbers,group)
print('Found: ', found)
print(numbers)
"""
Found:  False
[2, 3, 5, 7, 1, 4, 6, 8]
"""

print("\n Program number 3")
# using nonlocal to solve the problem in program number 2
def sort_priority3(numbers,group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found
numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
found = sort_priority3(numbers,group)
print("Found: ", found)
print(numbers)
"""
Found:  True
[2, 3, 5, 7, 1, 4, 6, 8]
"""

print("\nProgram number 4")
# using nonlocal it gets complicated 
# in such case use helper class
class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False
    
    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0,x)
        return (1,x)

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
sorter = Sorter(group)
numbers.sort(key=sorter)
print(numbers)
print(sorter.found)
"""
[2, 3, 5, 7, 1, 4, 6, 8]
True
"""


"""
=====CONCLUSION======
don't use nonlocal beyound simple function
"""
