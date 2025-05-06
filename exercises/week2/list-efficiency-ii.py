# Implement a test, where the numbers 1,2,\dots,n are added to the end of the list one at a time. Then 
# the first element of the list is deleted n times.

# Implement the test with n=10^5. Make two time measurements: How much time it takes to do all the 
# additions, and how much time to do all the deletions.

# In this task you get a point automatically when you fill in your measurement results and the code used
# in the test, and press the submit button.

# Time for additions:  0.04s
# Time for deletions:  0.04s

# The code you used in the test:
import time
import collections


def add_remove(n):
  nums = collections.deque()

  #append
  start_append = time.time()
  for i in range(1, n+1):
    nums.append(i)
  end_append = time.time()
  print("APPEND time:", round(end_append-start_append, 2), "s")

  #popleft
  start_pop = time.time()
  for _ in range(n):
    nums.popleft()
  end_pop = time.time()
  print("POP time:", round(end_pop-start_pop, 2), "s")

def test_time():
  n = 1000000

  start_time = time.time()
  result = add_remove(n)
  end_time = time.time()

  print("n", n)
  print("TOTAL timeL:", round(end_time-start_time, 2), "s")

test_time()