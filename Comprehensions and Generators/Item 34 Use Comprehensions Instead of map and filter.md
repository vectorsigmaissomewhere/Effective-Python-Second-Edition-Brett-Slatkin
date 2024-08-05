What is list comprehension?
```text
Python provides compact syntax for deriving a new list from another
sequence or iterable. These expressions are called comprehensions
```

Program number 1, Compute the square of each number in a list
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for x in a:
    squares.append(x ** 2)
print(squares) 
```

output
```text
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Program number 2, 
doing the same program using list comprehension
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)
```

output
```text
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Program number 3, 

For simple cases map required the creation of a lambda function for the computation which is visually noisy
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alt = list(map(lambda x: x ** 2, a))
print(alt)
```

output
```text
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Program number 4, 
```text
List comprehension easily let you to filter items from the input list
below prgram shows how to do this
square the numbers that are divisible by 2 using list comprehension
```
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in a if x % 2 == 0 ]
print(even_squares)
```

output
```text
[4, 16, 36, 64, 100]
```

Program number 5 
```text
square the number that are divisible by 2 using list comprehension, using filter built-in function can be using along with map
```
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alt = map(lambda x: x**2, filter(lambda x:x%2==0, a))
print(list(alt))
```
output
```text
[4, 16, 36, 64, 100]
```

Program number 6 
```text
dictionary and sets also have comprehension called dictionary comprehension and set comprehension
finding square using dictionary and cubes of number that is divisible by 3 in set
```
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
threes_cubed_set = {x**3 for x in a if x % 3 == 0}
print(even_squares_dict)
print(threes_cubed_set)
```
output
```text
{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
{216, 729, 27}
```

Prgram number 7 
```text
finding square using dictionary and cubes of number that is divisible by 3 in set using map and filter
```
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alt_dict = dict(map(lambda x: (x, x**2),
                    filter(lambda x:x%2==0, a)))
alt_set = set(map(lambda x: x**3,
                  filter(lambda x:x%3==0, a)))

print(alt_dict)
print(alt_set)
```

output
```text
{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
{216, 729, 27}
```

conclusion
```text
- list comprehension is clearer than the map and filter built-in functions because they don't required lambda expression
- list comprehension allows skipping item, map cannot without the use of filter 
- Dictionaries and sets can also by created using comprehensions
```
