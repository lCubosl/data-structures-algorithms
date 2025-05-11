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

# Running time when using a list: 27.744 s
# Running time when using a set:  0.008 s
# Running time when using a dictionary:  0.014 s

# The code used in the test:

import random
import time

# list
def count_distinct_list(numbers):
    seen = []
    start_time = time.time()
    for x in numbers:
        if x not in seen:
            seen.append(x)
    end_time = time.time()
    print("list time:", round(end_time-start_time, 3), "s")
    return seen

# set
def count_distinct_set(numbers):
    seen = set()
    start_time = time.time()
    for x in numbers:
        if x not in seen:
            seen.add(x)
    end_time = time.time()
    print("set time:", round(end_time-start_time, 3), "s")
    return seen

# dict
def count_distinct_dict(numbers):
    seen = {}
    count = 0
    start_time = time.time()
    for x in numbers:
        if x not in seen:
            seen[count] = x
            count += 1
    end_time = time.time()
    print("dict time:", round(end_time-start_time, 3), "s")
    return seen

n = 100000
#print("n: ", n)
random.seed(1337)

count_distinct_list([random.randint(1, 10**7) for _ in range(n)])
count_distinct_set([random.randint(1, 10**7) for _ in range(n)])
count_distinct_dict([random.randint(1, 10**7) for _ in range(n)])