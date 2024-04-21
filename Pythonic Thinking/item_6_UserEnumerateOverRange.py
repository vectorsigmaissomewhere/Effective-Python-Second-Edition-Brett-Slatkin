# Prefer enumerate over range

print('Example no 1')
## using randint to get randomly 0 and 1 bits
from random import randint

random_bits = 0
for i in range(32):
    if randint(0,1):
        random_bits |= 1 << i
print(bin(random_bits))

"""
0b11011111011101111111000000010111
"""

print('\nExample no 2')
## using a datastructure to iterate over it 
flavor_list = ['vanilla','chocolate','pecan','strawberry']
for flavor in flavor_list:
    print(f'{flavor} is delicious')

"""
vanilla is delicious
chocolate is delicious
pecan is delicious
strawberry is delicious
"""


print('\nExample no 3')
# priting the item using the index of the list
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i+1}: {flavor}')

"""
1: vanilla
2: chocolate
3: pecan
4: strawberry
""" 


print('\nExample no 4')
#using enumerate to print each element

it = enumerate(flavor_list)
print(next(it))
print(next(it))

"""
(0, 'vanilla')
(1, 'chocolate')
"""

print('\nExample no 5')
# using enumerate to print the index and the item

for i, flavor in enumerate(flavor_list):
    print(f'{i+1}: {flavor}')

"""
1: vanilla
2: chocolate
3: pecan
4: strawberry
""" 

print('\nExample no 6')
# using enumerate to print the index and the item with specified index

for i,flavor in enumerate(flavor_list,1):
    print(f'{i}: {flavor}')

"""
output
1: vanilla
2: chocolate
3: pecan
4: strawberry
"""

