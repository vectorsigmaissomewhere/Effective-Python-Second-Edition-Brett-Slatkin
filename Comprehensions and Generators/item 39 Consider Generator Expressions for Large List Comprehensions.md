# CONSIDER GENERATOR EXPRESSIONS FOR LARGE LIST COMPREHENSIONS 
```text
When to use list comprehension and when to use genrators
```

value = [int(x) for x in open('my_file.txt')]
print(value)

it = (int(x) for x in open('my_file.txt'))
print(it)
print(next(it))


roots = ((x, x**0.5) for x in it)
print(next(roots))
