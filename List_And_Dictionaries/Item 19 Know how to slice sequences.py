print("Program number 1")
# somelist[start:end] where start is inclusive and end is exclusive
a = ['a','b','c','d','e','f','g','h']
print('Middle two: ', a[3:5])
print('All but ends:',a[1:7])

# Middle two:  ['d', 'e']
# All but ends: ['b', 'c', 'd', 'e', 'f', 'g']


# ================  WHAT TO AVOID ====================
# here you should avoid using a[0:5]
print(a[:5] == a[0:5])
# True 

# leave out the final index
# avoid using a[a:len(a)]
print(a[5:] == a[5:len(a)])
# True

# Showing different types of slicing
print(a[:]) #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[:5]) # ['a', 'b', 'c', 'd', 'e']
print(a[:-1]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(a[4:]) # ['e', 'f', 'g', 'h']
print(a[-3:]) # ['f', 'g', 'h']
print(a[2:5]) # ['c', 'd', 'e']
print(a[2:-1]) # ['c', 'd', 'e', 'f', 'g']
print(a[-3:-1]) # ['f', 'g']

print("\n")
first_twenty_items = a[:20]
last_twenty_items = a[-20:]

print(first_twenty_items) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(last_twenty_items) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# ==============EXTRA =======================
print(a[-0:] == a[:]) # True 

print("\nProgram number 2")
# Modifying the result of slicing won't affect the original value
b = a[3:]
print('Before:    ',b)
b[1] = 99
print('After:      ',b)
print('NO change:',a)

# Before:     ['d', 'e', 'f', 'g', 'h']
# After:       ['d', 99, 'f', 'g', 'h']
# NO change: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


print("\nProgram number 3")
# Slicing replaces the specified range in the original list
print('Before ',a)
a[2:7] = [99,22,13]
print('After ',a)

# Before  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# After  ['a', 'b', 99, 22, 13, 'h']


print("\n")
# copying the original list
b = a[:]
print(b)
#['a', 'b', 99, 22, 13, 'h']


print("\nProgram no 4")
# allocating a new list VS copying the list
# Here we are copying the entire list 

b = a # if you don't want to copy the reference use b = a[:] to see what happens
print('Before a',a)
print('Before b',b)
a[:]  = [101,102,103]
print('After a', a)
print('Before b',b)

# After a [101, 102, 103]
# Before b [101, 102, 103]


#========================================CONCLUSTION========================
# Don't supply 0 for the start index or the length of the sequnce for the end index
