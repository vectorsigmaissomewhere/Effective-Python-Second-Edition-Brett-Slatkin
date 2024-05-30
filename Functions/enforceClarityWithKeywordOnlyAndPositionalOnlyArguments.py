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
