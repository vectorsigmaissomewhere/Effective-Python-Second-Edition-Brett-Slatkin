Accept functions instead of classes for simple interfaces

Example 1: Sort list of names baseed on their length by providing len build-in function as the key hook

```python
names = ['Socrates','Archimedes','Plate','Aristotle']
names.sort(key=len)
print(names) 
```

output
```text
['Plate', 'Socrates', 'Aristotle', 'Archimedes']
```

Example 2: 
```python
def log_missing():
    print('Key added')
    return 0

from collections import defaultdict
current = {'green':12, 'blue':3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]
result = defaultdict(log_missing, current)
print('Before:', dict(result))
for key, amount in increments: # if it finds a new key it calls the log_missing function
    result[key] += amount
print('After: ', dict(result))
```
output
```text
Before: {'green': 12, 'blue': 3}
Key added
Key added
After:  {'green': 12, 'blue': 20, 'red': 5, 'orange': 9}
```

=================Note where to use log_missing functions========================

```text
functions like log_missing makes APIs easy to build and test 

The default value hook passed to defaultdict to count the total number of keys that were missing
one way to do this is by using a stateful closure
Helper function that uses such a closure as the default value hook
```

```python
from collections import defaultdict

def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count # stateful closure
        added_count += 1
        return 0
    
    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    return result, added_count

current = {'green':12, 'blue': 2}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

result, count = increment_with_report(current, increments)
print(result)
print(count)
```
output
```text
defaultdict(<function increment_with_report.<locals>.missing at 0x00000213B716C540>, {'green': 12, 'blue': 19, 'red': 5, 'orange': 9})
2
```


Problem with defining a closure for stateful hooks is that it's harder to read than the stateless function example
```text
the above program and this program is similar
Define a small class that encapsulates the state you want to track
```

```python
from collections import defaultdict

class CountMissing:
    def __init__(self):
        self.added = 0
    
    def missing(self):
        self.added += 1
        return 0

current = {'green':12, 'blue': 2}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

counter = CountMissing()
result = defaultdict(counter.missing, current)
for key, amount in increments:
    result[key] += amount


print(counter.added) # 2
```

python allows classes to define the __call_ specal method.
```text
__call__ allows an object to be called just like a function
all objects that can be executed in this manner are referred to as callables
```
```python
from collections import defaultdict

class BetterCountMissing:
    def __init__(self):
        self.added = 0
    
    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
print(counter() == 0) # True 
print(callable(counter)) # True


current = {'green':12, 'blue': 2}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

counter = BetterCountMissing()
result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount

print(counter.added == 2) 
```
output
```text
True
```
Conclusion
```text
Closure
Use functions for simple interfaces instead of using classes 
references to functions and methods in Python are first class
The __call__ method enables instances of a class to be called like plain Python functions
When you need a function to maintain state, consider defining a class that provides the __call__method instead of defining a stateful closure
```
