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
