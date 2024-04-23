# Avoid else Blocks after for and while loops

print("Program no 1")
# shows how else block work
# as for loop ends else block statment runs

for i in range(3):
    print('Loop',i)
else:
    print('Else block!')

"""
Loop 0     
Loop 1     
Loop 2     
Else block!
"""

print("\nProgram no 2")
# use will break
# when we use break the else statement doesn't work 
for i in range(3):
    print('Loop',i)
    if i == 1:
        break
else:
    print('Else block!')

"""
Loop 0
Loop 1
"""


print("\nProgram no 3")
# when list is empty 
# else block statement executes

for x in []:
    print("Never runs")
else:
    print("For Else Block!")

"""
For Else Block!
"""

print("\n Program no 4")
# when the while statement is False

while False:
    print("Never runs")
else:
    print("While Else Block!")

"""
While Else Block!
"""


print("\n Program no 5")
# Coprime example
# Here the program never goes to if block and
# as a result the program never breaks and when the loop ends
# the statement goes to else block

a = 4
b = 9

for i in range(2,min(a,b)+1):
    print("Testing", i)
    if a % i == 0 and b % i == 0:
        print('Not comprime')
        break
else:
    print('Coprime')
"""
Testing 2
Testing 3
Testing 4
"""


print("\n Program no 6")
# we will use helper function 
# why ? to execute the result as soon as the condition matches

def coprime(a,b):
    for i in range(2,min(a,b)+1):
        if a%i == 0 and b%i == 0:
            return False
    return True

coprime(4,9)
assert not coprime(3,6)

"""
True 
"""

print("\n Program no 7")
# get the value as soon as possible set the is_coprime to False
# when the statment becomes true and breaks the program 
# and return the value

def coprime_alternate(a,b):
    is_coprime = True
    for i in range(2,min(a,b)+1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime

assert coprime_alternate(4,9)
assert not coprime_alternate(3,6)

"""

"""
