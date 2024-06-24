1 The problem 
```text
The order of iteration would not match the order in which the items were inserted
```
Code illustration
```python
baby_names = {
    'cat': 'kitten',
    'dog': 'puppy',
}

print(baby_names)
```

output
```text
output before python 3.6: {'dog': 'puppy', 'cat': 'kitten'} # reason of the swapping or random key being misplaced is because dictionary before implemented the hash table algorithm 
output in python 3.6: {'cat': 'kittem', 'dog': 'puppy'}
```

Before python3.6
```text
method like keys, values , items and popitems whould randomly make changes in the data structure
```

in python 3.6 it was improved 
```python 
print(list(baby_names.keys()))
print(list(baby_names.values()))
print(list(baby_names.items()))
print(list(baby_names.popitem()))
```

output
```text
['cat', 'dog']
['kitten', 'puppy']
[('cat', 'kitten'), ('dog', 'puppy')]
['dog', 'puppy']
```

2 About **kwargs
```text
**kwargs was following the same thing like dictionary before python3.6
```

working of **kwargs 
```python
def my_func(**kwargs):
    for key, value in kwargs.items():
        print('%s = %s' % (key, value))

my_func(goose='gosling',kangaroo='joey')
```

output before python3.6
```text
kangaroo = joey
goose = gosling
```

output after python 3.6
```text
goose = gosling
kangaroo = joey
```

3 Classes with the dict type for their instance dictionary 

```text
In previous version,
python object fields would show the same randomizing behavior
```
Code
```python
class MyClass:
    def __init__(self):
        self.alligator = 'hatchling'
        self.elephant = 'calf'
    
a = MyClass()
for key, value in a.__dict__.items():
    print('%s = %s' % (key, value))
```

output before python 3.6
```text
elephant = calf
alligator = hatchling
```
output in python 3.6 
```text
alligator = hatchling
elephant = calf
```

Note
```text
first note: 
you can now use this behaviour
to design api for your classes and functions

second note:
Use OrderedDict instead of python dict
to handle high rate of key insertions and popitem call
also before python3.6 OrderedDict was used to preserve the dictionary items ordering
```

4 Program to show the results of a contest for the cutest baby animal 
Code
```python 
votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863,
}

# this function prcess the voting data and saves the rank of each animal\
# name into a provided empty dictionary 
def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

# function which provide the first key as winnner
def get_winner(ranks):
    return next(iter(ranks))

ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)
```

output
```text
{'otter': 1, 'fox': 2, 'polar bear': 3}
otter
```

5 Show the results in alphabetical order
```text
To make this work we will use collections.abc to define a new dictionary-like class 
that iterates its content in alphabetical order
```

```python
from collections.abc import MutableMapping

class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]
    
    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key
    
    def __len__(self):
        return len(self.data)

votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863,
}

def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key = votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner(ranks):
    return next(iter(ranks))
    
sorted_ranks = SortedDict() # using SortedDict instance in place of standard dict, where assumption is no longer true
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)
```

output
```text
{'otter': 1, 'fox': 2, 'polar bear': 3}
fox
```

How to solve this problem 
```text
There are 3 ways to solve this problem 
but I will give you only one way to solve this problem
```
Solution 1: Reimplement the get_winner function
```python 
def get_winner(ranks):
    for name, rank in ranks.items():
        if rank == 1:
            return name
winner = get_winner(sorted_ranks)
print(winner)
```
output
```text
{'otter': 1, 'fox': 2, 'polar bear': 3}
otter
```
