# never unpack more than three variables 
# when functions return multiple values
# unpacking into four or more variables is 
# error prone and should be avoided 
# return a small class or namedtuple instead

print("Program no 1")
# unpacking variables from a function

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

lengths = [63,73,72,60,67,66,71,61,72,70]

minimum, maximum = get_stats(lengths)

print(f'Min: {minimum}, Max: {maximum}')

"""
output
Min: 60, Max: 73
"""

print("\nProrgam no 2")
# A simple program to demonstrate hwo unpacking works
def my_function():
    return 1,2

first, second = my_function()
assert first == 1
assert second == 2



print("\nProgram no 3")
# returning longest and shortes items individually 
# by using a starred expression for the middle portions 
# of the list

# what we learned is starred skips the mid value 
# and prints first and last item

def get_avg_ratio(numbers):
    average  = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

lengths = [63,73,72,60,67,66,71,61,72,70]
longest, *middle, shortest = get_avg_ratio(lengths)
print(f'Longest: {longest:>4.0%}')
print(f'Shortest: {shortest:>4.0%}')
"""
Longest: 108%
Shortest:  89%
"""



print("\nProgram no 4")
# writing a program that prints 
# minimum, maximum, average, median, count

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count

    sorted_numbers = sorted(numbers)
    middle = count // 2
    # if length of the list is odd
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median  = (lower + upper) / 2
    else: 
        median = sorted_numbers[middle]
    
    return minimum, maximum, average, median, count

lengths = [63,73,72,60,67,66,71,61,72,70,]
minimum, maximum, average, median, count = get_stats(lengths)

print(f'Min: {minimum}, Max: {maximum}')
print(f'Average: {average}, Median: {median}, Count {count}')

"""
Min: 60, Max: 73
Average: 67.5, Median: 68.5, Count 10
"""








"""
conclusion 
unpacking into four or more variables is 
error prone and should be avoided 

in program no 4
if you swap average and median 
minimum, maximum, average, median, count = get_stats(lengths)
value will also get swapped 
To avoid these problem you should never unpack multiple variable 
unpacking 3 variable is okay 
"""


