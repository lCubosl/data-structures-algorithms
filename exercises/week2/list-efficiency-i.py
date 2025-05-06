# Implement a test, where the numbers 1,2,\dots,n are added to the end of the list one at a time. Then 
# the last element of the list is deleted n times.

# Implement the test with n=10^5. Make two time measurements: How much time it takes to do all the 
# additions, and how much time to do all the deletions.

# In this task you get a point automatically when you fill in your measurement results and the code used 
# in the test, and press the submit button.

# Time for additions:  0.5s

# Time for deletions:  0.44s

# The code you used in the test:

import time

# n 100000
# result: None
# time: 0.01 s
def add(n):
  count = 0
  nums = []
  while count < n:
    nums.append(count)
    count += 1

# n 100000
# result: ([], -1)
# time: 35.85 s
def remove_n(n, remove_list):
  nums = remove_list
  count = n

  while len(nums) > 0:
    nums.remove(count)
    count -= 1

  return nums, count

# add and remove in the same function
def add_remove(n):
  nums = []
  # append
  start_append = time.time()
  for i in range(1, n+1):
    nums.append(i)
  end_append = time.time()
  print("append time:", round(end_append-start_append, 2), "s")

  # pop
  start_pop = time.time()
  for _ in range(n):
    nums.pop()
  end_pop = time.time()
  print("pop time:", round(end_pop-start_pop, 2), "s")
  
  return nums

def test_time():
  n = 10000000

  start_time = time.time()
  result = add_remove(n)
  end_time = time.time()

  print("n", n)
  print("time TOTAL:", round(end_time-start_time, 2), "s")

test_time()