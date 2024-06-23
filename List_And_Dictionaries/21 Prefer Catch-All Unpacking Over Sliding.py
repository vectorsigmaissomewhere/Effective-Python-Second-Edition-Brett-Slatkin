# Take first two of the list with basic unpacking
car_ages = [0,9,4,8,7,20,19,1,6,15]
car_ages_descending = sorted(car_ages,reverse=True)
# oldest, second_oldest = car_ages_descending
# this gives an error, too many values to unpack

# INDEXING AND SLICING 
# Extract the oldest, second oldest , and other car ages from a list 
print("\n Program number 1")
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest,second_oldest,others)
# output
"""
20 19 [15, 9, 8, 7, 6, 4, 1, 0]
"""
# the above program is noisy and is error prone


# Using starred expression to achieve the same result as above without indexing or slicing
print("\n Program number 2")
oldest, second_oldest, *others = car_ages_descending
print(oldest,second_oldest,others)
# output
"""
20 19 [15, 9, 8, 7, 6, 4, 1, 0]
"""

# extract one slice as starred expression can be used in any position
print("\n Program number 3")
oldest, *others, youngest = car_ages_descending
print(oldest,youngest,others)

*others,second_youngest,youngest = car_ages_descending
print(youngest,second_youngest,others)
# output
"""
20 0 [19, 15, 9, 8, 7, 6, 4, 1]
0 1 [20, 19, 15, 9, 8, 7, 6, 4]
"""

# =======NOTE===========
"""
you use startted expression , at least one part is required like
*others = cars_ages_descending # this expression will give you an error

*first, *others = somelist
this is also error prone you can't use two starred expression
"""


# using starred expression for unpacking multilevel structure
print("Program number 4")
car_inventory = {
    'Downtown': ('Silver Shadow','Pinto','DMC'),
    'Airport' : ('Skyline', 'Viper', 'Gremlin','Nova'),
}

((loc1, (best1,*rest1)),
 (loc2, (bestt2, *rest2))) = car_inventory.items()
print(f'Best at {loc1} is {best1}, {len(rest1)} others')
print(f'Best at {loc2} is {bestt2}, {len(rest2)} others')
# output
"""
Best at Downtown is Silver Shadow, 2 others
Best at Airport is Skyline, 3 others
"""

# check if there are no left over item in a list
print("\n Program number 5")
short_list = [1,2]
first, second, *rest = short_list
print(first,second,rest)
# output
"""
1 2 []
"""

# unpack arbitrary iterators with the unpacking suntax
# this is not useful
print("\n Program number 6")
it = iter(range(1,3))
first,second = it
print(f'{first} and {second}')
# output
"""
1 and 2
"""

# Generator that yields the rows of a CSV file containing all car orders from the dealership this week
print("\n Program number 7")
def generate_csv():
    yield ('Date','Make','Model','Year','Price')

all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print('CSV Header: ', header)
print('Row  count: ', len(rows))
# output
"""
CSV Header:  ('Date', 'Make', 'Model', 'Year', 'Price')
Row  count:  0
"""

# Unpacking with a starred expression makes it easy to process the first row
print('\n Program number 8')
it = generate_csv()
header, *rows = it
print('CSV Header:',header)
print('Row count: ',len(rows))
# output
"""
CSV Header: ('Date', 'Make', 'Model', 'Year', 'Price')
Row count:  0
"""
