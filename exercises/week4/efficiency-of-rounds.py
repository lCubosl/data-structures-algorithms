# In the course material, there is an example for week 4 of an algorithm using a dictionary for counting the rounds 
# needed to collect numbers from a list. Earlier in an exercise for week 2, the same task was solved using a list 
# instead of a dictionary.

# The auxiliary data structure used in the task can be either a list or a dictionary, because a number can be used 
# either as a list index or as a dictionary key. How does the choice of the data structure affect the efficiency of 
# the algorithm?

# Compare the efficiency of the two implementations for an input list containing the numbers 1,2,...,10^7 in a 
# random order.

# In this task you get a point automatically, when you fill in your results and the code you used, and press the 
# submit button.

# Running time when using a list:  ANSWER
# Running time when using a dictionary:  ANSWER

# The code used in the test:

# list
def count_distinct_list(numbers):
    seen = []
    for x in numbers:
        if x not in seen:
            seen.append(x)
    return seen

# set
def count_distinct_set(numbers):
    seen = set()
    for x in numbers:
        if x not in seen:
            seen.add(x)
    return seen

# dict
def count_distinct_dict(numbers):
    seen = {}
    count = 0
    for x in numbers:
        if x not in seen:
            seen[count] = x
            count += 1
    return seen

print(count_distinct_list([2,3,5,3,4,4,6,2]))
print(count_distinct_set([2,3,5,3,4,4,6,2]))
print(count_distinct_dict([2,3,5,3,4,4,6,2]))