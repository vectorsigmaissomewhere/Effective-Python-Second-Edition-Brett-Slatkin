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
