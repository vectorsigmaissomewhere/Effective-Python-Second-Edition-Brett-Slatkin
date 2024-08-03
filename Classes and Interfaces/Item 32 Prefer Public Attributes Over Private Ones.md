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

How classmethod can access private attributes
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
Output
```text
Why class methods that is get_private_field() method can acess the __private_field because
Class method have access to private attributes because they are declared within the surrounding class block.
```

Sub class cannot access it's parent class private attributes
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
