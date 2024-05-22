print("program number 1")
# Program to pass argument when calling a function
def remainder(number, divisor):
    return number % divisor

print(remainder(20,7))
"""
6
"""

print("program number 2")
# Program to pass argumnets and positional argument and mixed argument to see the output
remainder(20,7)  #6 argument
# print(remainder(20,divisor=7)) # this gives an error
print(remainder(number = 20, divisor = 7)) # 6 positional argument
print(remainder(divisor = 7, number = 20)) # 6 positional argument

print("Program number 3")
# using ** operator , dictionary , keyword argument or positional mixture
my_kwargs = {
    'number' : 20,
    'divisor' : 7
}
print(remainder(**my_kwargs)) # 6

print("Program number 4")
# mixture or positional argument and keyword argument
my_kwargs={
    'divisor': 7,
}
print(remainder(20,**my_kwargs)) #6

print("Program number 5")
# use ** operator multiple times if you know that the dictonaries don't contain overlapping keys
my_kwargs = {
    'number': 20,
}

other_kwargs = {
    'divisor': 7,
}

print(remainder(**my_kwargs,**other_kwargs)) #6

print("Program number 7")
# receive any named keyword argument
# use **kwargs catch-all parameter to collect these arguments into a dict 
# the process it
def print_parameters(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} = {value}')

print_parameters(alpha=1.5,beta=9,gamma=4)
# alpha = 1.5
# beta = 9
# gamma = 4


print("Program number 8")
# benefits of keyword function 
# you can define default value specified in the function defintion
# this is for one day 
def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print(f'{flow:.3} kg per second')

# 0.167 kg per second


print("Program number 9")
# this is for other days defined as period
def flow_rate(weight_diff, time_diff, period):
    return (weight_diff/ time_diff) * period
weight_diff = 0.5
time_diff = 3
flow_per_second = flow_rate(weight_diff, time_diff,period=1)
print(flow_per_second)

# 0.16666666666666666


print("Program number 10")
# making it less noisy 
# giving the period argument a default value
# period argument is now optional 
def flow_rate(weight_diff, time_diff,period = 1):
    return (weight_diff / time_diff) *period

flow_per_second = flow_rate(weight_diff,time_diff)
flow_per_hour = flow_rate(weight_diff,time_diff,period=1000)
print(flow_per_second)
print(flow_per_hour)

#  0.16666666666666666
#  166.66666666666666


print("Program number 11")
# this example shows how optional argument works
def flow_rate(weight_diff, time_diff,period = 1,units_per_kg = 1):
    return ((weight_diff * units_per_kg) / time_diff) * period

weight_diff = 0.5
time_diff = 3
pounds_per_hour = flow_rate(weight_diff,time_diff,period=3600,units_per_kg=2.2)
print(pounds_per_hour)
# 1320.0


# =============KEY TO REMEMBER ===================
# function arguments can be specified by position or by keyword
# keyword arguments with default values make it easy to add new behaviours to a function without 
# needing to migrate all existing callers
# Optional keyword arguments should always be passed by keyword instead of by position
