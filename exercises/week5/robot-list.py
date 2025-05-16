# You are given a list of integers. No number occurs more than once on the list.

# A robot starts at the location 0 and collects the numbers on the list in order from the smallest to the largest. Your task 
# is to compute how many steps the robot takes in total.

# For example, when the list is [42, 1337, 1, 10^9], the robot moves as follows:

# 2 steps to the right (number 1)
# 2 steps to the left (number 42)
# 1 step to the right (number 1337)
# 2 steps to the right (number 10^9)

# In this case, the robot takes 2+2+1+2=7 steps.

# In a file robolist.py, implement the function count_steps that takes a list of integers as a parameter and returns the number of steps taken by the robot.

# You should implement the function so that it computes the step count efficiently even for long lists. The function should finish immediately in the last test case of the code template too.

# O(n x m)
def count_steps(numbers):
  ordered = sorted(set(numbers))
  list_i = []
  count = 0

  for i, num in enumerate(ordered):
    idx = numbers.index(num)
    list_i.append(idx)

    if i > 0 :
      prev_idx = numbers.index(ordered[i-1])
      count += abs(idx - prev_idx)
    else:
      count = idx

  return count

# O(n)
def count_steps(numbers):
  index_map = {num: i for i, num in enumerate(numbers)}
  ordered = sorted(index_map.keys())
  
  count = 0
  for i, num in enumerate(ordered):
    idx = index_map[num]

    if i > 0 :
      prev_idx = index_map[ordered[i - 1]]
      count += abs(idx - prev_idx)
    else:
      count = idx

  return count

print(count_steps([1])) # 0
print(count_steps([1, 2, 3])) # 2
print(count_steps([3, 2, 1])) # 4
print(count_steps([42, 1337, 1, 10**9])) # 7
print(count_steps([1, 3, 5, 7, 8, 6, 4, 2])) # 28
print(count_steps([10**6, 10**8, 10**7, 10**9])) # 5

numbers = [(x * 999983) % 10**9 + 1 for x in range(10**5)]
print(count_steps(numbers)) # 4871908997