Program number 1 
```text
As a new orderw come in from customers, 
Tell the customer whether you can fulfill the orders or not
Also verify that a request is sufficiently in stock and above the minimum threshold for shipping
```
```python
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']
def get_batches(count, size):
    return count // size

result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches
print(result)
```
output
```text
{'screws': 4, 'wingnuts': 1}
```

Program number 2
```text
same as program number 1 but 
Using the lopping logic more clearly using dictionary comprehensions
```
```python
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']
def get_batches(count, size):
    return count // size

result = {}
found = {name: get_batches(stock.get(name, 0), 8)
        for name in order
        if get_batches(stock.get(name, 0), 8)}

print(found)
```
output 
```text
{'screws': 4, 'wingnuts': 1}
```
```text
# problem with program number 2 is
# the get_batches method is repeated which hurts readability
```
program number 3
```text
in program number 3, changed the first get_batches call to have 4 as its second parameter instead of 8 
which causes the results to be different
```

```python
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']
def get_batches(count, size):
    return count // size

result = {}
has_bug = {name : get_batches(stock.get(name, 0), 4)
           for name in order
           if get_batches(stock.get(name, 0), 8)}
print('Expected:', found) # from program number
print('Found: ', has_bug)
```
output
```text
Expected: {'screws': 4, 'wingnuts': 1}
Found:  {'screws': 8, 'wingnuts': 2}
```

Program number 4
```text
Solving the problem of program number  by using walrus operators
```
```python
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']
def get_batches(count, size):
    return count // size

result = {}
found = {name: batches for name in order
         if (batches := get_batches(stock.get(name, 0), 8))}
print(found)
```
output
```text
{'screws': 4, 'wingnuts': 1}
```
Program number 5 
```python
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']
def get_batches(count, size):
    return count // size

result = {}
result = {name: tenth for name, count in stock.items()
          if (tenth := count // 10) > 0}
print(result)
```
output
```text
{'nails': 12, 'screws': 3, 'washers': 2}
```

Program number 6
```python
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']
def get_batches(count, size):
    return count // size

half = [(last := count // 2) for count in stock.values()]
print(f'Last item of {half} is {last}')
```
output
```text
Last item of [62, 17, 4, 12] is 12
```

Program number 7 
```text
Loop leak
```
```python
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']
def get_batches(count, size):
    return count // size

for count in stock.values(): # Leaks loop variable
    pass
print(f'Last item of {list(stock.values())} is {count}')
```
output
```text
Last item of [125, 35, 8, 24] is 24
```

Program number 8 
```python
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']
def get_batches(count, size):
    return count // size

found = ((name, batches) for name in order
         if (batches := get_batches(stock.get(name,0), 8)))
print(next(found))
print(next(found))
```
output
```text
('screws', 4)
('wingnuts', 1)
```
