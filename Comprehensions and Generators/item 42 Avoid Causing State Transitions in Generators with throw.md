
```text
In addition to yield from expressions and the send method another advanced
generator feature is the throw method for re-raising Exception instances within 
generator functions.

When the method is called, the next occurence of a yield expression re-raises the 
provided Exception Instance after its output is received Instead of continuing 
normally
```

Program number 1
```python
class MyError(Exception):
    pass

def my_generator():
    yield 1
    yield 2
    yield 3

it = my_generator()
print(next(it))
print(next(it))
print(it.throw(MyError('test error')))
```

output
```text
1
2
MyError: test error
```

Program number 2
```text
Surround yield expression with try/except compound statement
Also, 
This is an example of two-way communication channel between a 
generator and its caller 
```

```python
class MyError(Exception):
    pass

def my_generator():
    yield 1
    try:
        yield 2
    except MyError:
        print('Got MyError!')
    else:
        yield 3
    yield 4

it = my_generator()
print(next(it)) # yield 1
print(next(it)) # yield 2 
print(next(it)) # yield 3
print(next(it)) # yield 4
```

output
```text
1
2
3
4
```

Program number 3
```text
Program with a timer that supports sporadic resets
Implement this behavior by defining a generator that relies on the throw method
```

```python
class Reset(Exception):
    pass

def timer(period):
    current = period 
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period 
    # Whenever the Reset exception is raised by the yield expression
    # the counter resets itself to its original period 

def check_for_reset():
    # Poll for external event

def announce(remaining):
    print(f'{remaining} ticks remaining')

# drive the timer generator which injects exceptions with throw to cause resets
# or calls announce for each generator output
def run():
    it = timer
    while True:
        try:
            if check_for_reset():
                current = it.throw(Result())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)

run()
```
output
```text
Need to check this program 
```

Reason why Program number 2 is noisy
```text
various level of nesting required to catch StopIteration exception or 
decide to throw call next or 
announce make the code noisy
```

Program 3
```text
Making Program number 2 less noisy
Define a stateful closure using an Iterable container object
Redefine the timer generator by using such a class
```

```python
class Timer:
    def __init__(self, period):
        self.current = period
        self.period = period
    
    def reset(self):
        self.current = self.period
    
    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current
    
    def check_for_reset():
        pass
    
    # Iteration using for statement
def run():
    timer = Timer(4)
    for current in timer:
        if check_for_reset():
            timer.reset()
        announce(current)

run()
```

output
```text

```

```text
You can do this thing in much better way using 
asynchronous function
```
Things to remember
```text
- The throw method can be used to re-raise exception within 
generators at the position of the most recently executed yield 
expression.
- Using throw harms readability because it required additional nesting 
and boilterplate in order to raise and catch exceptions.
- A better way to provide exceptional behavior in generators is to use
a class that implements the __iter__ method along with methods to cause
exceptional state transitions.
```
