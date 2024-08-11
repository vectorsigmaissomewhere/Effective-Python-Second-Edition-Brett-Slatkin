About this section
```text
A common pattern with comprehension with list, dict, and set variants is
the need to reference the same computation in multiple places
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
