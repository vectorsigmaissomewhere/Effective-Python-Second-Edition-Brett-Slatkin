Two types of visibility for class attributes
```text
- Public 
- Private
```

Program number 1 to demonstrate public and private attributes
```python
class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field

foo = MyObject()
print(foo.public_field == 5)
print(foo.get_private_field()==10)
# print(foo.__private_field==5) # Exception 
```

Output
```text
True 
True
```

Conclusion
```
Third print statement gives an error, 
```

Program number 2 How classmethod can access private attributes
```python
class MyOtherObject:
    def __init__(self):
        self.__private_field = 71
    
    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field

bar = MyOtherObject()
print(MyOtherObject.get_private_field_of_instance(bar) == 71)
```
Output
```text
True
```
Conclusion
```text
Why class methods that is get_private_field() method can acess the __private_field because
Class method have access to private attributes because they are declared within the surrounding class block.
```

Program number 3 Sub class cannot access it's parent class private attributes
```python
class MyParentObject:
    def __init__(self):
        self.__private_field = 71

class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field

baz = MyChildObject()
#baz.get_private_field() # this gives and error 
print(baz._MyParentObject__private_field == 71) # this don't give an error to know why,  check the below conclusion
print(baz.__dict__) # to check the names after the transformation
```
Output
```text
Error 
True 
{'_MyParentObject__private_field': 71}
```

Conclusion
```text
Here private attribute real name is _MyParentObject__private_field
Accessing the parent's private attribute from the child class fails simply because the transformed attribute name 
doesn't exist 

When MyChildObject tries to access the attribute it's name is _MyChildObject__private_field instead of 
_MyParentObject__private_field
```

Program number 4
```text
You can do anything with the objects
Protected fields are protected by convention meaning external users of the class should proceed with caution.
New python programmers use private fields to indicate an internal API that shouldn't be accessed by subclasses or externally
```

```python
class MyStringClass:
    def __init__(self, value):
        self.__value = value
    
    def get_value(self):
        return str(self.__value)

foo = MyStringClass(5)
print(foo.get_value() == '5')
```

output
```text
True
```

Conclusion
```text
This is a wrong way to do so 
As even you will add subclass and so you won't be able to access the private fields
```


Program number 5, How to acess the private fields
```python
class MyIntegerSubClass(MyStringClass):
    def get_value(self):
        return int(self._MyStringClass__value)

foo = MyIntegerSubClass('5')
print(foo.get_value() == 5)
```

Output
```text
True
```

Program number 6, Here the IntegerSubClass class's immediate parent, MyStringClass has had another parent class added called MyBaseClass
```python
class MyBaseClass:
    def __init__(self, value):
        self.__value = value
    
    def get_value(self):
        return self.__value
    
class MyStringClass(MyBaseClass):
    def get_value(self):
        return str(super().get_value()) # Updated

class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        return int(self._MyStringClass__value) # updated

foo1 = MyStringClass(5)
print(foo1.get_value())  # 5
foo = MyIntegerSubClass(5)
print(foo.get_value()) # 5
```

output
```text
5
5
```

Program number 7
```text
To extend your code safely err on the side of allowing subclasses to do more by using protected attributes
Document each protected field and explain which fileds are internal APIs available to subclasses and which should be left alone 
```

```python
class MyStringClass:
    def __init__(self, value):
        # This stores the user-supplied value for the object.
        # It should be coercible to a string. Once assigned in 
        # the object it should be treated as immutable
        self._value = value
        # and so on rest of the program 
```

Program number 8
```text
Time to seriously consider using private attributes is when you're worried about naming conflicts with subclasses
```

```python
class ApiClass:
    def __init__(self):
        self._value = 5
    
    def get(self):
        return self._value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello' # conflict 

a = Child()
print(f'{a.get()} and {a._value} should be different')
```

output
```text
hello and hello should be different
```

Program number 9 
```text
To reduce the risk of the above issue occuring, 
you can use a private attribute in the parent class to ensure that there are no attribute 
names that overlap with child classes
```

```python
class ApiClass:
    def __init__(self):
        self.__value = 5 # Double underscore

    def get(self):
        return self.__value # Double underscore

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello' # ok!

a = Child()
print(f'{a.get()} and {a._value} are different')
```

output
```text
5 and hello are different
```

Whole Conclusion
```text
for protected files use documentation
consider using private attributes to avoid naming conflicts with subclasses that are out of your control
```
