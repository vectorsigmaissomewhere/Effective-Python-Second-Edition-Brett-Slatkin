Inherit from collections.abc for Custom Container Types

```Text
class contain data and describbes how such objects relate to each other
Every Python class is a container of some kind, encapsulating attributes and functionality together
Python build-in container types for managing data: lists, tuples, sets and dictionaries.
```
Program number 1
```text
Custom list type that has additional methods for counting the frequency of its members
```
```python
class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right

class IndexableNode(BinaryNode):
    def _traverse(self):
        if self.left is not None:
            yield from self.left._traverse()
        yield self
        if self.right is not None:
            yield from self.right._traverse()
    
    def __getitem__(self, index):
        for i, item in enumerate(self._traverse()):
            if i == index:
                return item.value
        raise IndexError(f'Index {index} is out of range')
    
    def __contains__(self, value):
        return any(item.value == value for item in self._traverse())

class SequenceNode(IndexableNode):
    def __len__(self):
        count = 0
        for _ in self._traverse():
            count += 1
        return count

# Tree construction
tree = SequenceNode(
    10, 
    left=SequenceNode(2),
    right=SequenceNode(
        6,
        right=SequenceNode(7)
    )
)

# Access like a list in addition to traversing the tree with the left and right attributes
print('Index 0 is', tree[0])
print('Index 1 is', tree[1])
print('Index 2 is', tree[2])
print('11 in the tree?', 11 in tree)
print('17 in the tree?', 17 in tree)
print('Tree is', [node.value for node in tree._traverse()])

# Print the length of the tree
print('Tree length is', len(tree))

# implementing all the methods from abstract base class from collections.abc, as I did above with SequenceNode
# It provides all the additional methods like index and counrt for free

from collections.abc import Sequence

class BetterNode(SequenceNode, Sequence):
    pass

tree = BetterNode(
    10, 
    left=BetterNode(2),
    right=BetterNode(
        6, 
        right=BetterNode(7)
    )
)

print('Index of 7 is', tree.index(7))
print('Count of 10 is', tree.count(10))
````
output
```text
Index 0 is 2
Index 1 is 10
Index 2 is 6
11 in the tree? False
17 in the tree? False
Tree is [2, 10, 6, 7]
Tree length is 4
Index of 7 is 3
Count of 10 is 1
```
