Three fundamental operations for interacting with dictionaries
```text
Accessing Keys
Assigning Keys
Deleteing Keys
```

1 Example no one to determine people' favorite types of breed to devise the menu for a sandwich shop
```text
increment the counter value
to do so, 
- see if the key exists 
- insert the key with a default counter value of zero if it's missing
- and increment the couter value wih 1
```
```python
counters = {
    'pumpernickel': 2,
    'sourdough': 1,
}
key = 'wheat'

if key in counters:
    count = counters[key]
else:
    count = 0
counters[key] = count + 1
for key,value in counters.items():
    print(key,value)
```
output
```text
pumpernickel 2
sourdough 1
wheat 1
```
about the above program 
```
if the above program what we did is check if the key exists or not 
as it don't exist we incremented the value by 1
```

2 Another way to do the same behavior on how dictionaries raise a keyError exception when you try to get the value a key that doesn't exist
```python
counters = {
    'pumpernickel': 2,
    'sourdough': 1,
}
key = 'wheat'
try:
    count = counters[key]
except KeyError:
    count = 0
counters[key] = count + 1
for key,item in counters.items():
    print(key,item)
```
output
```text
pumpernickel 2
sourdough 1
wheat 1 
```

3 Program for counting votes
```python
counters = {
    'powernickel': 2,
    'sourdough': 1,
}

key = 'wheat'

# since key is not in counters value of wheat incremented to 1
if key not in counters:
    counters[key] = 0
counters[key] += 1 

# since key is in counters value of wheat is incremented to 2
if key in counters:
    counters[key] += 1
else:
    counters[key] = 1
# since key is present no exception is raised
try:
    counters[key] += 1
except KeyError:
    counters[key] = 1

for key,value in counters.items():
    print(key,value)
```
output
```text
powernickel 2
sourdough 1
wheat 3
```
NOTE
```text
better use Counter class from the collections for maintaining dictionaries like this
````

The above program was to count the votes

about program number 4
```text
now making changes to values of dictionaries of more complex types
like a list
```

4 Program to know who voted for what type of breed
```python
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}

key = 'brioche'
who = 'Elmer'

if key in votes:
    names = votes[key]
else:
    votes[key] = names = [] # we can even write this in two lines
names.append(who)
print(votes)
```
output
```text
{'baguette': ['Bob', 'Alice'], 'ciabatta': ['Coco', 'Deb'], 'brioche': ['Elmer']}
```

5 Making program number 4 more efficient by using KeyError exception instead of using in
```python
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}

key = 'brioche'
who = 'Elmer'

try:
    names = votes[key]
except KeyError:
    votes[key] = names = []
names.append(who)
print(votes)
```

output
```text
{'baguette': ['Bob', 'Alice'], 'ciabatta': ['Coco', 'Deb'], 'brioche': ['Elmer']}
```

6 Other ways of making program number 4 more efficient
```python
one way: 
# using get method to fetch a list value when the key is present
names = votes.get(key) # getting the values of a key in dictionary 
if names is None:
     votes[key] = names = []
names.append(who)

two way: 
# using walrus operator to make the get method fetching process shorter
if (names := votes.get(key)) is None:
    votes[key] = names = []
names.append(who)

third way:
# using setdefault method which makes the program even more shorter
# first it checks if the key is present or not
# if the key is not present if gives a default value
# a quick demo
names = votes.setdefault(key, [])
names.append(who)
```

7 In example number 6 the third way of using setdefault method creates a program 
``text

```
code explaination
```python
data = {}
key = 'foo'
value = []
data.setdefault(key, value)
print('Before:', data)
value.append('hello')
print('After:', data)
```

output
```text
Before: {'foo': []}
After: {'foo': ['hello']}
```
