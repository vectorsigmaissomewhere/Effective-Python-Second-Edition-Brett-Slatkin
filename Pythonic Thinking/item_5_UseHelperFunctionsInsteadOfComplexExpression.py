# Using helper function instead of complex expressions

from urllib.parse import parse_qs

print('first statement')
my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)
print(repr(my_values))

# in python any thing being empty or 0 means False
print('\nsecond statement')
# we don't have opacity key so we will get None
print('Red: ',my_values.get('red'))
print('Green: ',my_values.get('green'))
print('Opacity: ',my_values.get('opacity'))

# using this trick, in python any thing being empty or 0 means False
# here green is empty so we get 0 and opacity key is not present
print('\nThird Statement')
red = my_values.get('red',[''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity',[''])[0] or 0
print(f'Red: {red!r}')
print(f'Green: {green!r}')
print(f'Opacity: {opacity!r}')

# The above code that we are seeing is hard to read
# Now we will us if/else ternary expression to make it more clear
# in single statement
print('\nFourth Statement')
red_str = my_values.get('red',[''])
red = int(red_str[0] if red_str[0] else 0)
print(red)


# Using the same if else in multiple statement
print('\nFIfth Statement')
green_str = my_values.get('green',[''])
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0
print(green)


# to solve this now we will us helper function
# break complex expression in small pieces
print('\nSixth Statement')
def get_first_int(values,key,default=0):
    found = values.get(key,[''])
    if found[0]:
        return int(found[0])
    return default

green = get_first_int(my_values,'green')
print(green)


"""
output
first statement
{'red': ['5'], 'blue': ['0'], 'green': ['']}

second statement
Red:  ['5']
Green:  ['']
Opacity:  None

Third Statement
Red: '5'
Green: 0
Opacity: 0

Fourth Statement
5

FIfth Statement
0

Sixth Statement
0

"""

