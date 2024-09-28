```text
The itertools built-in module contains a large number of functions
that are useful fo organizing and interacting with iterators.

To deal with iterators problem see itertools documentation
```

Important functions that you should know in three primary categories
```text
1. Linking Iterators Together
- chain
- repeat
- cycle
- tee
- zip_longest

2. Filtering Items from an Iterator
- islice
- takewhile
- dropwhile
- filterfalse

3. Producing Combinations of Items from Iterators
- accumulate
- product 
- permutations
- combinations
- combinations_with_replacement 
```

1.1 chain
```text
Use chain to combine multiple iterators into a single sequential iterator
```

```python
import itertools 
it = itertools.chain([1, 2, 3], [4, 5, 6])
print(list(it))
```

output
```text
[1, 2, 3, 4, 5, 6]
```

1.2 repeat
```text
Use repeat to output a single value forever, or 
use the second paramter to specify a maximum number of times
```

```python
import itertools
it = itertools.repeat('hello', 3)
print(list(it))
```

output
```text
['hello', 'hello', 'hello']
```

1.3 cycle
```text
Use cycle to repeat an iterator items forever
```

```python
import itertools
it = itertools.cycle([1,2])
result = [next(it) for _ in range(10)]
print(result)
```
output
```text
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
```

1.4 tee
```text
Use tee to split  a single iterator into the number of parallel iterators 
The memory usuage of this function will grow if the iterators don't progress at the same speed
as buffering will be required to enqueue the pending items
```
```python
import itertools
it1, it2, it3 = itertools.tee(['first', 'second'], 3)
print(list(it1))
print(list(it2))
print(list(it3))
```

output
```text
['first', 'second']
['first', 'second']
['first', 'second']
```

1.5 zip_longest
```text
This function returns a placeholder value when an iterator is exausted, 
which may happen if iterators have different lengths.
```
```python
import itertools
keys = ['one', 'two', 'three']
values = [1, 2]

normal = list(zip(keys, values))
print('zip:       ', normal)

it = itertools.zip_longest(keys, values, fillvalue='nope')
longest = list(it)
print('zip_longest: ', longest)
```
output
```text
zip:        [('one', 1), ('two', 2)]
zip_longest:  [('one', 1), ('two', 2), ('three', 'nope')]
```

2 Filtering Items from an Iterator

2.1 islice
```text
Use islice to slice an iterator by numerical indexes without copying.
You can specify end, start, start and end, or start, end, step sizes 
```

```python
import itertools
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_five = itertools.islice(values, 5)
print('First five: ', list(first_five))
middle_odds = itertools.islice(values, 2, 8, 2)
print('Middle odds: ', list(middle_odds))
```

output
```text
First five:  [1, 2, 3, 4, 5]
Middle odds:  [3, 5, 7]
```

2.2 takewhile
```text
takewhile returns items from an iterator until a predicate function returns False for an item
```

```python
import itertools
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x : x < 7
it = itertools.takewhile(less_than_seven, values)
print(list(it))
```

output
```text
[1, 2, 3, 4, 5, 6]
```

2.3 dropwhile
```text
dropwhile is the oppposite of takewhile.
skips items from an iterator until the predicate function returns True for the first time
```

```python
import itertools
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x : x < 7
it = itertools.dropwhile(less_than_seven, values)
print(list(it))
```

output
```text
[7, 8, 9, 10]
```

2.4 filterfalse
```text
filterfalse is the opposite of the filter built-in function.
returns all items from an iterator where a predicate funcion returns False
```

```python
import itertools
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = lambda x : x % 2 == 0
filter_result = filter(evens, values)
print('Filter:     ', list(filter_result))
filter_false_result = itertools.filterfalse(evens, values)
print('Filter false: ', list(filter_false_result))
```
output
```text
Filter:      [2, 4, 6, 8, 10]
Filter false:  [1, 3, 5, 7, 9]
```

3. Producing Combinations of Items from Iterators
```text
The itertools built-in module includes a number of functions for producing 
combinations of items from iterators
```

3.1 accumulate
```text
accumulate folds an item from the iterator into a running value by applying a function that takes 
two paramters.
It outputs the current accumulated result for each input value.
```

```python
import itertools
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_reduce = itertools.accumulate(values)
print('Sum:     ', list(sum_reduce))

def sum_modulo_20(first, second):
    output = first + second
    return output % 20

module_reduce = itertools.accumulate(values, sum_modulo_20)
print('Modulo: ', list(module_reduce))
```

```output
Sum:      [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
Modulo:  [1, 3, 6, 10, 15, 1, 8, 16, 5, 15]
```

3.2 product
```text
product returns the Catesian product of items from one or more iterators, 
which is a nice alternative to using deeply nested list comprehensions 
```

```python
import itertools
single = itertools.product([1,2], repeat = 2)
print('Single: ', list(single))

multiple = itertools.product([1,2], ['a', ' b'])
print('Multiple:', list(multiple))
```

```output
Single:  [(1, 1), (1, 2), (2, 1), (2, 2)]
Multiple: [(1, 'a'), (1, ' b'), (2, 'a'), (2, ' b')]
```

3.3 permutations
```text
permutations returns the unique ordered permutations of length N
with items from an iterator
```

```python
import itertools
it = itertools.permutations([1, 2, 3, 4], 2)
print(list(it))
```

output
```text
[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
```

3.4 Combinations
```text
Combinations returns the unordered combinations of length N with unrepeated items from an iterator
```

```python
import itertools
it = itertools.combinations([1, 2, 3, 4], 2)
print(list(it))
```

output
```text
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

3.5 combinations_with_replacement
```text
combinations_with_replacement is the same as combinations, but repeated values are allowed
```

```python
import itertools
it = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
print(list(it))
```
output
```text
[(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
```
Things to remember
```text
- The itertools functions falls into three main categories
- More functions and tools are available in documentions
```
