Avoid More than two control subexpressions in comprehension

Program number 1: Example: Simplify a matrix into one flat list of all cells
```text
Comprehension supports multiple levels of looping
Do this by a list of comprehension by including two for subexpressions
These subexpressions run in the order provided from left to right
```

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)
```
```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Program number 2
```text
Replicating the two-level-deep layout of the input list
noisy becuase of [] character, but it's still relatively easy to read
```
```python
squared = [[x**2 for x in row] for row in matrix]
print(squared)
```
```text
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
```

Program number 3: 
three loop for this list comprehension
```text
three level list comprehension
```
```python
my_lists  = [[[1,2,3], [4,5,6,],  [7,8,9]]]
flat = [x for sublist1 in my_lists for sublists2 in sublist1 for x in sublists2]
print(flat)
```
```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Program number 4
```text
same result using normal loop statements
The indentation of this version makes the looping clearer
```
```python
my_lists  = [[[1,2,3], [4,5,6,],  [7,8,9]]]
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)
print(flat)
```
```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Program number 5 
```text
showing comprehensions supporting multiple if conditions 
filter a list of numbers to only even values greater than 4 
These two list comprehensions are equivalent
```
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]
print(a)
print(b)
print(c)
```
```text
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[6, 8, 10]
[6, 8, 10]
```

Program number 6 
```text
Filter a matrix so that the only cells remaining are those divisible by 3 in rows that sum to 10 or higher
avoid using list, set, dict comprehension that look like this
```
```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
filtered = [[x for x in row if x % 3 ==0]
            for row in matrix if sum(row) >= 10]
print(filtered)
```
```text
[[6], [9]]
```

Rule of thumb
```text
avoid using more than two control subexpressions in a comprehension
that can be two conditions, two lops or one condition and one loop 
if it gets more complicated that this start using normal if and for loop and write a helper function
```

Conclusion
```text
- Comprehensions support multiple levels of loops and multiple conditions per loop level 
- Comprehensions with more than two control subexpressions are very difficult and should be avoided
```
