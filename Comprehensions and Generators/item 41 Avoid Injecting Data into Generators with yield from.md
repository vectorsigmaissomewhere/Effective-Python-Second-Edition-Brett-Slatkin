Note:
```text
Amplitude is a peak point of a wave function
```
```text
yield expression have generator functions
This generator function produces an iterable series of output values.

You cannot in and out data in generator function in bidirectional communication
```

Program number 1
```text
A program that transmits signals using a software defined radio.

In this program, We have a function
that generates an sine wave with a given number of points
```

```python
import math

def wave(amplitude, steps):
    step_size = 2 * math.pi / steps 
    print(f'Step size: {step_size}')
    print('start of the first iteration')
    print('it will iterate 8 times as value of steps is 8')
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output # here run function is called # and run function calls transmit one by 
    
def transmit(output):
    if output is None:
        print(f'Output is None')
    else:
        print(f'Output: {output:>5.1f}')

def run(it):
    for output in it:
        transmit(output)

run(wave(3.0,8))   
```

output
```text
Step size: 0.7853981633974483
start of the first iteration
it will iterate 8 times as value of steps is 8
Output:   0.0
Output:   2.1
Output:   3.0
Output:   2.1
Output:   0.0
Output:  -2.1
Output:  -3.0
Output:  -2.1
```

Program number 2
```text
Python generators have send method.
Using send method you can send data in bidirectional 
That is input and output.
Send method takes input and at the same time yields output.

Note: When iterating a generator the value of the yield expression is None.
```
```python
def my_generator():
    received = yield 1
    print(f'received = {received}')

it = iter(my_generator())
output = next(it) # Get first generator method
print(f'output = {output}')

try:
    next(it)
except StopIteration:
    pass
```
output
```text
output = 1
received = None
```

Program number 3 
```text
Using send function, the supplied paramter becomes the 
value of the yield expression when the generator is resumed.

When generator starts, 
a yield expression has not been encountered yet, 
so the only valid value for calling send initially is None
```

````python
def my_generator():
    received = yield 1
    print(f'received = {received}')

it = iter(my_generator())
output = it.send(None) # Get first generator output
print(f'output = {output}')

try:
    it.send('hello!')
except StopIteration:
    pass
```

output
```text
output = 1
received = hello!
```

Program number 4
```text
What to do to modulate the amplitude of the sine wave based 
on an input signal?
First, change the wave generator to save the amplitude returned 
by the yield expression
Second, use it to calulate the next generated output:
```

```python
import math

def wave_modulating(steps):
    step_size = 2 * math.pi / steps 
    amplitude = yield # Receive initial amplitude
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output # Receive next amplitude 

# update the run function to stream the modulating amplitude
# into the wave_modulating generator on each iteration.

# first input to send must be None, since a yield expression 
# would not have occured within the generator yet

def run_modulating(it):
    amplitudes = [None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)

def transmit(output):
    if output is None:
        print(f'Output is None')
    else:
        print(f'Output: {output:>5.1f}')

run_modulating(wave_modulating(12))
```

output
```text
Output is None
Output:   0.0
Output:   3.5
Output:   6.1
Output:   2.0
Output:   1.7
Output:   1.0
Output:   0.0
Output:  -5.0
Output:  -8.7
Output: -10.0
Output:  -8.7
Output:  -5.0
```

Program number 5
```text
Using multiple signals
```

```python
import math

def wave_modulating(steps):
    step_size = 2 * math.pi / steps 
    amplitude = yield # Receive initial amplitude
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output # Receive next amplitude 

# update the run function to stream the modulating amplitude
# into the wave_modulating generator on each iteration.

# first input to send must be None, since a yield expression 
# would not have occured within the generator yet

def run_modulating(it):
    amplitudes = [None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)

def transmit(output):
    if output is None:
        print(f'Output is None')
    else:
        print(f'Output: {output:>5.1f}')

def complex_wave_modulating():
    yield from wave_modulating(5)
    yield from wave_modulating(3)
    yield from wave_modulating(3)

run_modulating(complex_wave_modulating())
```

output
```text
Output is None
Output:   0.0
Output:   6.7
Output:   4.1
Output:  -1.2
Output:  -1.9
Output is None
Output:   0.0
Output:   8.7
Output:  -8.7
Output is None
Output:   0.0
Output:   8.7
```
```text
Why do we have many None value?
Don't think about it cause the program with using send method is too complex
```
Easiest solution without using send method

Program number 6

```text
Step 1 - Pass iterator to the wave function
The iterator returns an input amplitude each time the next built-in function is called
Each generator is progressed in a cascade as inputs and outputs are processed
```

```python
import math 

def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it) # Get next input
        output = amplitude * fraction
        yield output

# pass iterator into each of the generator function 
# iterators are stateful and thus each of the nested generators picks up 
# where the previous generator left off

def complex_wave_cascading(amplitude_it):
    yield from wave_cascading(amplitude_it, 3)
    yield from wave_cascading(amplitude_it, 4)
    yield from wave_cascading(amplitude_it, 5)

# running the composed generator by simply passing in an iterator from the amplitudes list
def run_cascading():
    amplitudes = [7 ,7 ,7 ,2 ,2 ,2 ,2 ,10 ,10 ,10 ,10]
    it = complex_wave_cascading(iter(amplitudes))
    for amplitude in amplitudes:
        output = next(it)
        transmit(output)

def transmit(output):
    if output is None:
        print(f'Output is None')
    else:
        print(f'Output: {output:>5.1f}')

run_cascading()
```

output
```text
Output:   0.0
Output:   6.1
Output:  -6.1
Output:   0.0
Output:   2.0
Output:   0.0
Output:  -2.0
Output:   0.0
Output:   9.5
Output:   5.9
Output:  -5.9
```
```text
Here the iterator can come from anywhere and are completely dynamic
Here, input generator is not thread safe. Use async functions to cross thread boundaries
```
Conclusion
```text
- The send method can be used to inject data into a generator by giving
the yield expression a value that can be assigned to a variable.
- Using send with yield from expressions may cause surprising behavior,
Such as None values appearing at unexpected times in the generator output.
- Providing an input iterator to a set of composed generators is a better
approach than using the send method, which should be avoided.
```
