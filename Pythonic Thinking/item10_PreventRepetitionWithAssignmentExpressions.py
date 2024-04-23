# Prevent Repetition with Assignment Expression 
# Quick review of assignment expression and walrus operator 
# Assignment Expression 
# a = b
# Walrus Operator
# a := b

# Overal question is of juice bar 


print("Question no 1")
# we will use lemon in this case 
# When a customer comes to make lemonde 
# There must be one lemon in the basket
fresh_fruit = {
    'apple' : 10,
    'banana' : 8,
    'lemon' : 5,
}

def make_lemonde(count):
    print(f"We have created lemonde with {count} lemons")

def out_of_stock():
    print("There is no lemons for lemonde")

count = fresh_fruit.get('lemon',0)
if count:
    make_lemonde(count)
else:
    out_of_stock()

"""
We have created lemonde with 5 lemons
"""

print("Question no 2")
# The above code looks noisier 
# So, we will use walrus operator and 
# solve the same question
fresh_fruit = {
    'apple' : 10,
    'banana' : 8,
    'lemon' : 5,
}

def make_lemonde(count):
    print(f"We have created lemonde with {count} lemons")

def out_of_stock():
    print("There is no lemons for lemonde")

if count := fresh_fruit.get('lemon',0):
    make_lemonde(count)
else:
    out_of_stock()

"""
We have created lemonde with 5 lemons
"""


print("Question no 3")
# we will use apple in this case 
# There must be 4 apple in the basket to, 
# make a cider

fresh_fruit = {
    'apple' : 10,
    'banana' : 8,
    'lemon' : 5,
}

def make_cider(count):
    print(f"Your apple cider has been created with {count} apples")

def out_of_stock():
    print("There is no 4 apples")

count = fresh_fruit.get('apple',0)
if count >= 4:
    make_cider(count)
else:
    out_of_stock()

"""
Your apple cider has been created with 10 apples
"""


print("Question no 4")
# we will use walrus operator to solve 
# 3 number question
fresh_fruit = {
    'apple' : 10,
    'banana' : 8,
    'lemon' : 5,
}

def make_cider(count):
    print(f"Your apple cider has been created with {count} apples")

def out_of_stock():
    print("There is no 4 apples")

if (count := fresh_fruit.get('apple',0)) >=4:
    make_cider(count)
else:
    out_of_stock()

"""
Your apple cider has been created with 10 apples
"""

    
print("Question no 5")
# we will use banana in this case 
# There must be 2 banana to make a slice 

fresh_fruit = {
    'apple' : 10,
    'banana' : 8,
    'lemon' : 5,
}

def slice_bananas(count):
    return 2 

class OutOfBananas(Exception):
    pass

def out_of_stock():
    print("There is no 2 bananas") 

def make_smoothies(count):
    if count < 2:
        raise OutOfBananas
    print("Enjoy your smoothies")

pieces = 0
count = fresh_fruit.get('banana',0)
if count >= 2:
    pieces = slice_bananas(count)
try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

"""
Enjoy your smoothies
"""

print("Question no 6")
# Solve the same problem with 
# pieces in else block

fresh_fruit = {
    'apple' : 10,
    'banana' : 8,
    'lemon' : 5,
}

def slice_bananas(count):
    return 2 

class OutOfBananas(Exception):
    pass

def out_of_stock():
    print("There is no 2 bananas") 

def make_smoothies(count):
    if count < 2:
        raise OutOfBananas
    print("Enjoy your smoothies")

count = fresh_fruit.get('banana',0)
if count >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

"""
Enjoy your smoothies
"""


print("Question no 7")
# We will solve the same 5 and 6 number question 
# We will use walrus operator
# Here will not use else statement and 
# the pieces variable will be at the top

fresh_fruit = {
    'apple' : 10,
    'banana' : 8,
    'lemon' : 5,
}

def slice_bananas(count):
    return 2 

class OutOfBananas(Exception):
    pass

def out_of_stock():
    print("There is no 2 bananas") 

def make_smoothies(count):
    if count < 2:
        raise OutOfBananas
    print("Enjoy your smoothies")

pieces = 0
if (count := fresh_fruit.get('banana',0)) >= 2:
    pieces = slice_bananas(count)

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

"""
Enjoy your smoothies
"""


print("Question no 8")
# We will solve the same 5 and 6 number question 
# We will use walrus operator
# Here will use else statement and 
# the pieces variable will be in else statement

fresh_fruit = {
    'apple' : 10,
    'banana' : 8,
    'lemon' : 5,
}

def slice_bananas(count):
    return 2 

class OutOfBananas(Exception):
    pass

def out_of_stock():
    print("There is no 2 bananas") 

def make_smoothies(count):
    if count < 2:
        raise OutOfBananas
    print("Enjoy your smoothies")

if (count := fresh_fruit.get('banana',0)) >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()


"""
Enjoy your smoothies
"""

print("Question no 9")
# If customer want to print the fruits juice in sequence 
# priority list is banana, apple, lemon
fresh_fruit = {
    'apple' : 10,
    'banana' : 8,
    'lemon' : 5,
}

def slice_bananas(count):
    return 2 

class OutOfBananas(Exception):
    pass

def out_of_stock():
    print("There is no 2 bananas") 

def make_smoothies(count):
    if count < 2:
        raise OutOfBananas
    print("Enjoy your smoothies")

def make_cider(count):
    print(f"Your apple cider has been created with {count} apples")

def out_of_stock():
    print("There is no 4 apples")

def make_lemonde(count):
    print(f"We have created lemonde with {count} lemons")

def out_of_stock():
    print("There is no lemons for lemonde")

count = fresh_fruit.get('banana',0)
if count >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit.get('apple',0)
    if count >= 4:
        to_enjoy = make_cider(count)
        print(to_enjoy)
    else:
        count = fresh_fruit.get('lemon',0)
        if count:
            to_enjoy = make_lemonde(count)
            print(to_enjoy)
        else:
            to_enjoy = 'Nothing'
            print(to_enjoy)

"""
Enjoy your smooties
"""

print("Question no 10 ")
# The above way is the ugly way to use if else
# Now we will use walrus operator 
# and will solve the same problem

fresh_fruit = {
    'apple' : 10,
    'banana' : 8,
    'lemon' : 5,
}

def slice_bananas(count):
    return 2 

class OutOfBananas(Exception):
    pass

def out_of_stock():
    print("There is no 2 bananas") 

def make_smoothies(count):
    if count < 2:
        raise OutOfBananas
    print("Enjoy your smoothies")

def make_cider(count):
    print(f"Your apple cider has been created with {count} apples")

def out_of_stock():
    print("There is no 4 apples")

def make_lemonde(count):
    print(f"We have created lemonde with {count} lemons")

def out_of_stock():
    print("There is no lemons for lemonde")

if(count := fresh_fruit.get('banana',0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif(count := fresh_fruit.get('apple',0)) >= 4:
    to_enjoy = make_cider(count)
elif(count := fresh_fruit.get('lemon',0)):
    to_enjoy = make_lemonde(count)
else:
    to_enjoy = 'Nothing'







