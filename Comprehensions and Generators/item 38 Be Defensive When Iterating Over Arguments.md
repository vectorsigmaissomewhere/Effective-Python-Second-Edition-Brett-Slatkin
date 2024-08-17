Program number 1
```python
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
print(sum(percentages) == 100.0)
```
output
```text
11.538461538461538, 26.923076923076923, 61.53846153846154]
True
```
