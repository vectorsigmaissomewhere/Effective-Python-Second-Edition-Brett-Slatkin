Program number 1
```text
Find index of every word in a string
```
```python
def index_words(text):
    result = []
    if text:
        result.append(0)
    # finds the space, finds the index of the space and save it with increment
    # which will be the index of the word
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:10]) 
```
output
```text
[0, 5, 11, 15, 21, 27]
```
```text
Problem with prgram number 
The code are really dense and huge 
130 characters without whitespace while only 75 are important
one life for appending to the list and next for returning 
```

Program number 2
```text
One good way to write this function is by using a generator
Generators are produced by functions that use yield expressions
Generator function
while called a generator function immediately returns an iterator
each value passed to yield by the generator is returned by the iterator to the caller
this program can crash for larger inputs
```
```python
def index_words_iter(text):
    if text:
        yield 0 
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1
    
address = 'Four score and seven years ago...'
it = index_words_iter(address)
print(next(it))
print(next(it))
# You can easily convert the iterator returned by the generator
# to a list by passing it to the list built-in function if necessay
result = list(index_words_iter(address))
print(result[:10])
```
output
```text
0
5
[0, 5, 11, 15, 21, 27]
```

Program number 3
```text
Generator that streams input from a file one line at a time and yields outputs one word at a time
```
```python
import itertools
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

with open('address.txt', 'r') as f:
    it = index_file(f)
    results = itertools.islice(it, 0, 10)
    print(list(results))
```
output
```text
[0, 10, 15, 23, 29, 34, 36, 41, 45, 50]
```

Things to remember
```text
use generators instead of a function return a list
The iterator returned by a generator produces the set of values
passed to yield expressions within the generator function's body
```
