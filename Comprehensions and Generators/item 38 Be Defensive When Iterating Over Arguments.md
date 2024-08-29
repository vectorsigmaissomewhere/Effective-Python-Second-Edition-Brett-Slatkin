Program number 1
```text
A function that takes a list of objects as a parameter.
Here analyze tourism numbers for the U.S. state of Texas.
Imagine the list i.e the data set is the number of visitors
to each city(in milliona per year).
I'd like to figure out what percentage of overall tourism each city receives.

To do this,
we have a normalization function that sums the input to
determine the total number of tourists per year and
then divides each city's individual visitor counts
by the total to find that city's contribution to the whole.
```
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
program number 2
```text
To scale this up, I need to read the data from a file that
contains every city in all of Texas.
I define a generator to do this because then I can
reuse the same function later
In output
You will get an empty list because
an iterator produces its results only
a single time.
If you iterate over an iterator or a generator that has
already raised a StopIteration exception,
you won't get any results the second time around.
```
```python
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result
    
def read_visits(data_path):
  with open(data_path) as f:
      for line in f:
          yield int(line)

it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)
```
my_numbers.txt
```text
15
30
80
```
output
```text
[]
```
Program number 3 
```text
Reason on why you get this because
an iterator produces its results only a single time.,
If you iterate over an iterator or a generator that has
already raised a StopIteration exception, you won't get any results
the second time around:

But here, no StopIteration exception is raised
These functions can't tell the difference between
an iterator that has no output and an iterator
that had output and is now exhausted.
```
```python
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result
    
def read_visits(data_path):
  with open(data_path) as f:
      for line in f:
          yield int(line)

it = read_visits('my_numbers.txt')
print(list(it))
print(list(it))
```
output
```text
[15, 30, 80]
[]
```
program number 4
```text
To solve program number 3 problem
This is the same function as before, but it defensively copies the input iterator
```
```python
def normalize_copy(numbers):
    numbers_copy = list(numbers) # copy the iterator
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)
    return result

def read_visits(data_path):
  with open(data_path) as f:
      for line in f:
          yield int(line)

# Now the function works correctly on the read_visits generator's return value
it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)
print(sum(percentages) == 100.0)
```
output
```text
[12.0, 24.0, 64.0]
True
```

Program number 5
```text
Proram with program number 4 is that 
input iterator content can be exteremly large 
this could cause the program to run out of memory and crash
To solve this accept a function that returns a new iterator each time it's called
```

```python
def normalize_func(get_iter):
    total = sum(get_iter()) # New iterator
    result = []
    for value in get_iter(): # New iterator
        percent = 100 * value / total
        result.append(percent)
    return result
# to use normalize_func pass a lambda expression that calls
# the generator and produces a new iterator each time
path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
print(percentages)
print(sum(percentages) == 100.0)
```
output
```text
[11.538461538461538, 26.923076923076923, 61.53846153846154]
```

Program number 6
```python
class ReadVists:
    def __init__(self, data_path):
        self.data_path = data_path
    
    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)
print(sum(percentages)==100.0)
```
output
```text
[11.538461538461538, 26.923076923076923, 61.53846153846154]
```

Program number 6
```python
def normalize_defensive(numbers):
    if iter(numbers) is numbers:
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result
```

Program number 7
```python
from collections.abc import Iterator

def normalize_defensive(numbers):
    if isinstance(numbers, Iterator): # Another way to check
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize_defensive(visits)
print(sum(percentages)==100.0)
visits = ReadVisits(path)
percentages = normalize_defensive(visits)
print(sum(percentages)==100.0)

visits = [15, 35, 80]
it = iter(visits)
normalize_defensive(it)
```
