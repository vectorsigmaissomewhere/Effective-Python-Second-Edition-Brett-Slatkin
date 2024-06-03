print("Program number 1")
# be careful about special cases
# ignore OverflowError exceptions and return zero instead
# this function is straightforward.
# This call ignores the float overflow from division and returns zero
def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division(1.0, 10**500, True, False)
print(result)
# 0
# this call ignores the error from dividing by zero and returns inf
result = safe_division(1.0,0,False,True)
print(result) 
#inf


print("\nProgram number 2")
# it is easy to confuse the position of the two boolean arguments
# that control the exception-ignoring behavior
# this can easily cause bugs that are hard to tack down
# =========ONE WAY TO IMPROVE READABILITY IS TO USE KEYWORD ARGUMENTS============
def safe_division_b(number,divisor, ignore_overflow=False,ignore_zero_division=False):
    try:
        return number/divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division_b(1.0,10**500,ignore_overflow=True)
print(result)
# 0

result = safe_division_b(1.0,0,ignore_zero_division=True)
print(result)

# inf

#=================WHAT WE LEARNED FROM ABOVE PROGRAM===================
# we can still calling it with the old way , both of the program are same


print("\nPROGRAM NUMBER 3")
# defining function with keyword-only-arguments
# these arguments can only be suppliced by keyword and never by position
# SEPERATING THE POSITIONAL ARGUMENT AND KEYWORD-ONLY ARGUMENT WITH SYMBOL *

def safe_division_c(number,divisor,*,ignore_overflow=False,ignore_zero_division=False):
    try:
        return number/divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise
# safe_division_c(1.0,10**500,True,False) # takes only two positional argument but 4 are given 
# this will give an expection

result = safe_division_c(1.0,0,ignore_zero_division=True)
print(result)
# inf

print("\nPROGRAM NUMBER 4")
# here the / Symbol indicates where positional argument ends
def safe_division_d(numerator,denominator,/,*,ignore_overflow=False,ignore_zero_division=False):
    try:
        return numerator/denominator
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division_d(2,5)
print(result)
# o.4

# ===============THE MOST IMPORTANT THING=========================
print("\n PROGRAM NUMBER 5")
# the paramter name between the / and * symbols indicate that the argument can be passed by position or by keyword
def safe_division_e(numerator,denominator,/,ndigits=10,*,ignore_overflow=False,ignore_zero_division=False):
    try:
        fraction = numerator/denominator
        return round(fraction,ndigits)
    except OverflowError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division_e(22,7)
print(result)

result = safe_division_e(22,7,5)
print(result)

result = safe_division_e(22,7,ndigits=2)
print(result)

# 3.1428571429
# 3.14286
# 3.14
    

# =====================================CONCLUISION=============================
# keyword only argument forces callers to supply certain arguments by keyword only
# positional only argument ensures that calles can't supply certain paramters using keywords 
# means positional onlly arguments are defined before a single / in the argument list

# parametes between the / and * characters in the argument list can be supplied by position or keyword 
