# You are given a list of intervals, and your task is to count how many of the intervals are nested inside another interval.

# An interval (a,b) consists of the integers a,a+1,\dots,b. For example, the interval (3,7) consists of the integers 
# 3,4,5,6,7. An interval (a_1,b_1) is nested inside an interval (a_2,b_2) if a_2 \le a_1 and b_1 \le b_2. For example, the 
# intervals (4,6), (3,4) and (5,7) are all nested inside the interval (3,7).

# For example, for the list [(3,7),(1,2),(2,8),(1,4)] the desired answer is 2, because the intervals (3,7) and (1,2) are 
# nested inside another interval. The interval (3,7) is nested inside the interval (2,8), and the interval (1,2) is nested 
# inside the interval (1,4).

# In a file intervals.py, implement the function count_nested that takes a list of intervals as a parameter and returns the 
# number of nested intervals. You may assume that no two intervals on the list are the same.

# You should implement the function so that it runs efficiently even for long lists. The function should finish immediately in 
# the last two test cases of the code template too.

import random

def count_nested(intervals):
  pass

print(count_nested([])) # 0
print(count_nested([(1, 2)])) # 0
print(count_nested([(1, 2), (3, 4)])) # 0
print(count_nested([(1, 3), (2, 4)])) # 0
print(count_nested([(1, 4), (2, 3)])) # 1
print(count_nested([(1, 4), (1, 3)])) # 1
print(count_nested([(1, 4), (2, 4)])) # 1
print(count_nested([(1, 1), (1, 2), (1, 3)])) # 2
print(count_nested([(1, 6), (2, 5), (3, 4)])) # 2
print(count_nested([(1, 4), (2, 5), (3, 6)])) # 0

intervals = [(x+1, x+3) for x in range(10**5)]
random.shuffle(intervals)
print(count_nested(intervals)) # 0

intervals = [(x+1, 2*10**5-x) for x in range(10**5)]
random.shuffle(intervals)
print(count_nested(intervals)) # 99999    

