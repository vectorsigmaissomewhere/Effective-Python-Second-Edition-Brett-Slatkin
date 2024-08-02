old simple way to initialize parent class from child class

The problem 
```text
The problem with the basic way :
- The __init__ call order isn't specified across all subclasses
- One disadvantage here is, It is difficult for new readers to read the code
```

```python
class MyBaseClass:
    def __init__(self, value):
        self.value = value

class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)

class TimesTwo:
    def __init__(self):
        self.value *= 2
    
class PlusFive:
    def __init__(self):
        self.value += 5

class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self,value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

foo = OneWay(5)
print('First ordering value is (5 * 2) + 5 = ', foo.value)
```
output
```text
the output: First ordering value is (5 * 2) + 5 =  15
```

Diamond Inheritance
```text
Diamond Inheritance happens when a subclass inherits from two seperate classes that have the same 
superclass somewhere in the hierarchy .
```

Problem with diamond Inheritance
```text
cause superclass __init__ method run multiple times, causing unexpected behavior
```

```python
class TimesSeven(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self,value)
        self.value *= 7

class PlusNine(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 9

class ThisWay(TimesSeven, PlusNine):
    def __init__(self, value):
        TimesSeven.__init__(self, value)
        PlusNine.__init__(self, value)

foo = ThisWay(5)
print('Should be (5*7) + 9 = 44 but is', foo.value)
```

output
```text
Should be (5*7) + 9 = 44 but is 14
```

Why this value
```text
the second constructor PlusNone, overwrites the self.value values
This behavior is surprising and there is a way to solve this problem 
```

Solution for this
```text
To solve this Using super and standard method resolution order (MRO) 
The MRO defines ordering in which superclasses are initialized following an algorithm called C3 linearization.
Create a diamond shaped class hierarchy again but this time use super to initialize the parent class
Here the MyBaseClass.__init__ is run only a single time 
```

```python
class MyBaseClass:
    def __init__(self, value):
        self.value = value

class TimesSevenCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 7

class PlusNineCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9

class GoodWay(TimesSevenCorrect, PlusNineCorrect):
    def __init__(self, value):
        super().__init__(value)

foo = GoodWay(5)
print('Should be 7 *(5 + 9) = 98 and is ', foo.value)
```
output
```
Should be 7 *(5 + 9) = 98 and is  98
```

But it should be 
```text
(5 * 7) + 9 = 44 
```

Reason for this
```text
but it should be (5 * 7) + 9 = 44 
why opposite ordering 
how the calling happens here 
calls GoodWay, calls TimesSevenCorrect.__init__(), calls PlusNineCorrect.__init__() , calls MyBaseClass.__init__()
once it reaches to the top of the diamond , all the initialization does their work in the opposite order
```

Three ways to write the program like of the upper subclass like the same thing 
```python
# first way 
class ExplicitTrisect(MyBaseClass):
    def __init__(self, value):
        super(ExplicitTrisect, self).__init__(value)
        self.value /= 3

# second way 
class AutomaticTrisect(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value)
        self.value /= 3

# third way 
class ImplicitTrisect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value /= 3

print(ExplicitTrisect(9).value)
print(AutomaticTrisect(9).value)
print(ImplicitTrisect(9).value)
```

output
```
3.0
3.0
3.0
```

Conclusion
```text
- Python standard method resolution order solves the problems of superclass initialization order and diamond inheritance
- Use the super built-in function with zero arguments to initalize parent classes
```

