# Use zip to process Iterators in parallel

print("Program no 1")
# Question, create a list and print the length of the list
names = ['Cecilia','Lise','Marie']
counts = [len(n) for n in names]
print(counts)
 
"""
output
[7, 4, 5]

"""

print("\nProgram no 2")
# Question, iterate and print the list item with longest length
names = ['Cecilia','Lise','Marie']
counts = [len(n) for n in names]
longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)

"""
Cecilia
"""

print("\nProgram no 3")
# in program no 2 we are iterating into array for two times
# we will use enumerate to improve it slightly
names = ['Cecilia','Lise','Marie']
counts = [len(n) for n in names]
longest_name = None
max_count = 0

for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)

"""
Cecilia
"""

print("\nProgram no 4")
# here we will use zip to wraps two or more iterators with a lazy generator
names = ['Cecilia','Lise','Marie']
counts = [len(n) for n in names]
longest_name = None
max_count = 0

for name,count in zip(names,counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)

"""
Cecilia
"""

print("\nProgram no 5")
# here will update the list and try to get all the items
# but we will get not get the updated item 
# as count is not updated
names = ['Cecilia','Lise','Marie']
counts = [len(n) for n in names]
longest_name = None
max_count = 0

names.append("Rosalind")
for name,count in zip(names,counts):
    print(name)

"""
Cecilia 
Lise
Marie
"""

print("\nProgram no 6")
# in previous program I didn't get all the items
# now I will use zip_longest function from itertools to get all the items 
# even if the counts is not updated
# fills the count with whatever but the default is none
import itertools
names = ['Cecilia','Lise','Marie']
counts = [len(n) for n in names]
longest_name = None
max_count = 0

names.append("Rosalind")
for name,count in itertools.zip_longest(names,counts):
    print(f'{name}: {count}')


"""
Cecilia: 7  
Lise: 4     
Marie: 5
Rosalind: None
"""


