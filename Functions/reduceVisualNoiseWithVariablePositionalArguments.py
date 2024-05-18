# positional arguments are called varargs or star args
print('program number 1')
# log some infomation with fixed number of arguments 
def log(message,value):
    if not value:
        print(message)
    else:
        values_str = ','.join(str(x) for x in value)
        print(f'{message}: {values_str}')
    
log('My numbers are',[1,2])
log('Hi there',[])
"""
My numbers are: 1,2
Hi there
"""

print('\nprogram number 2')
# when second argumnets is empty 
# prefix the last positional argument with *
def log(message, *values):
    if not values:
        print(message)
    else:
        value_str = ','.join(str(x) for x in values)
        print(f'{message}: {value_str}')

log('My numbers are', 1, 2)
log('Hi there')
"""
My numbers are: 1,2
Hi there
"""

print('\nprogram number 3')
# the optional argument are always turned into tuple 
# before they are passed to a funcion
def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)
"""
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
"""

print('\n program number 4')
# user *args where the
# list will be reasonably small
def log(sequence, message, *values):
    if not values:
        print(f'{sequence} - {message}')
    else:
        value_str = ','.join(str(x) for x in values)
        print(f'{sequence} - {message} : {value_str}')

log(1, 'Favorites', 7, 33)
log(1, 'Hi there')
log('Favorite numbers', 7, 33)
"""
1 - Favorites : 7,33
1 - Hi there
Favorite numbers - 7 : 33
"""
# here we have bug which is undetectable 
# means *args can introduce hard to detect bugs
