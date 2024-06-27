1 Keep track of the cities that has been visited
```python
visits = {
    'Mexico': {'Tulum', 'Puerto Vallarta'},
    'Japan': {'Hukone'},
}

visits.setdefault('France', set()).add('Aries') 
# this can be done in long way 
"""
if (Japan := visits.get('Japan)) is None:
    visits['Japan'] = Japan = set()
Japan.add('Kyoto')
"""
print(visits)
```

```output
{'Mexico': {'Puerto Vallarta', 'Tulum'}, 'Japna': {'Hukone'}, 'France': {'Aries'}}
```

2 Program to wrao the example above in  a class with helper method to access the dynamic inner state stored in a dictionary

about the code
```text
It constructs a new set instance on every call, 
and it doesn't matter if the country was already present or not 
```
code
```python
class Visits:
    def __init__(self):
        self.data = {}
        
    def add(self, country, city):
        city_set = self.data.setdefault(country, set())
        city_set.add(city)

visits = Visits()
visits.add('Russia','Yekaterinburg')
visits.add('Tanzania', 'Zanzibar')
print(visits.data)
```

output
```text
{'Russia': {'Yekaterinburg'}, 'Tanzania': {'Zanzibar'}}
```

3 Solving the program number 2 problem using defaultdict class

about the problem 
```text
defaultdict class from the collections built-in module simplifies this common use case 
by automatically storing a default value when a key doesn't exist

provide a function that will return the default value to use each time a key is missing

using defaultdict class the code can assume that accessing any key in the data dictionary will
always result in the existing set instance.
```
Visits class to use defaultdict
```python
from collections import defaultdict

class Visits:
    def __init__(self):
        self.data = defaultdict(set)
    
    def add(self,country, city):
        self.data[country].add(city)
    
visits = Visits()
visits.add('England', 'Bath')
visits.add('England', 'London')
print(visits.data)
```
output
```text
defaultdict(<class 'set'>, {'England': {'London', 'Bath'}})
```

conclusion
```text
first conclusion:
if you are managing an arbitrary set of potential keys, then you should prefer using a defaultdict instance
from the collections build-in module if it suits your problem 
second conclusion
when a dictionary of arbitrary keys is passed to you, and you don't control its creation, 
in this case you should prefer the get method to access its items
third conclusion
use setdefault method in certain situation to make the code shorter
```
