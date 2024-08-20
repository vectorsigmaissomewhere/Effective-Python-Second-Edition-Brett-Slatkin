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
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)
```
output
```text
[]
```
