## use list built-in method to order the items in list

little intro
```python
# using sort to list integers from smallest to largest
numbers = [93,86,11,68,70]
numbers.sort()
print(numbers)
```

output
```text
[11, 68, 70, 86, 93]
```

1 Use the lambda keyword to define a function for the key parameter that enables me to sort the list of Tool objects albhabetically by their name

```python
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'

tools = [
    Tool('level', 3.5),
    Tool('hammer',1.25),
    Tool('screwdriver',0.5),
    Tool('chisel',0.25),
]
# tools.sort() not supported by the instances of 'Tool'
print('Unsorted:', repr(tools))
tools.sort(key=lambda x:x.name)
print('\nSorted:   ',tools)
```
output
```text
Unsorted: [Tool('level', 3.5), Tool('hammer', 1.25), Tool('screwdriver', 0.5), Tool('chisel', 0.25)]

Sorted:    [Tool('chisel', 0.25), Tool('hammer', 1.25), Tool('level', 3.5), Tool('screwdriver', 0.5)]
```

2 Define another lambda function to sort by weight and pass it as the key parameter to the sort method

```python
tools.sort(key=lambda x:x.weight)
print('By weight: ',tools)
```

```text
By weight:  [Tool('chisel', 0.25), Tool('screwdriver', 0.5), Tool('hammer', 1.25), Tool('level', 3.5)]
```

3 Using sort method in strings
```text
first sorted with Case sensitive 
and then sorted with Case insensitive
```

```python
places = ['home', 'work', 'Paris', 'home', 'work']
places.sort()
print('Case sensitive: ', places)
places.sort(key=lambda x: x.lower())
print('Case insensitive:', places)
```

```text
Case sensitive:  ['Paris', 'home', 'home', 'work', 'work']
Case insensitive: ['home', 'home', 'Paris', 'work', 'work']
```

4 Take tuple comparison behavior in order to sort the list of power tools first by weight and then by name
```python
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
     
    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'

power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]

power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)
```
output
```text
[Tool('drill', 4), Tool('sander', 4), Tool('circular saw', 5), Tool('jackhammer', 40)]
```

5 use reverse paramter in the sort function
```python
power_tools.sort(key = lambda x: (x.weight, x.name), reverse=True) # reverse makes all criteria descending
print(power_tools)
```
output
```text
[Tool('jackhammer', 40), Tool('circular saw', 5), Tool('sander', 4), Tool('drill', 4)]
```

6 Use unary minus operator in the key function, this reverse the sort order

about
```text
sort weight desceding and then 
sort name ascending 
```

```python
power_tools.sort(key = lambda x: (-x.weight, x.name))
print(power_tools)
# unary is not possible for certain type
# power_tools.sort(key = lamda x : (x.weight, -x.name),reverse=True) # error 
```

output
```text
[Tool('jackhammer', 40), Tool('circular saw', 5), Tool('drill', 4), Tool('sander', 4)]
```

7 For types that can't be negated, combine many sorting criteria together by calling the sort method multiple times using different key functions and reverse values, in the order of lowest rank sort call to highest rank sort call.

```python
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'

power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]

power_tools.sort(key=lambda x: x.name) # name ascending 
power_tools.sort(key=lambda x: x.weight,reverse=True) # weight descending
print(power_tools)
```

output
```text
[Tool('jackhammer', 40), Tool('circular saw', 5), Tool('drill', 4), Tool('sander', 4)]
```

How this worked 
```python 
# first sorting the names in alphabetical order
power_tools.sort(key=lambda x: x.name)
print(power_tools)
```
output
```text
[Tool('circular saw', 5), Tool('drill', 4), Tool('jackhammer', 40), Tool('sander', 4)]
```

```python
# sorting the weight by descending order
power_tools.sort(key=lambda x: x.weight,reverse=True)
print(power_tools)
```
```text
[Tool('jackhammer', 40), Tool('circular saw', 5), Tool('drill', 4), Tool('sander', 4)]
```

## Conclusion
```text
sort method
sort method with parameter
sort method with unary minues operator
sort method multiple times

Use unary negation to sort orders for simplicity
```
