# Sorting
# sorting is a classical algorithmic problem where the goal is to reorder the elements according to their
# value. There are efficient algorithms for sorting O(n logn)

# sorting in Python
numbers = [4,2,1,2]
numbers.sort()
print(numbers)
print("--------------------------------------------------")

# in addition, python has the function sorted
numbers = [4,2,1,2]
print(sorted(numbers))
print("--------------------------------------------------")

# the difference between the 2 ways of sorting a list is that the method sort modifiest the list
# while the function sorted creates a new list and leaves the original unmodified
# time complexity for both is O(nlogn)

# Example: smallest difference
# You are given a list of numbers. What is the smallest difference between two elements?
# list = [4,1,7,3,9], a=1
def min_dif(nums):
  nums =  sorted(nums)

  res = nums[1] - nums[0]
  for i in range(2, len(nums)):
    res = min(res, nums[i] - nums[i-1])
  return res

print(min_dif([4,1,7,3,9]))
print("--------------------------------------------------")
# algorithm first sorts and then computes the smallest difference
# sorting takes O(nlogn) and going through list takes O(n)
# total time complexity = O(n log n)

# Avoiding side effects
def min_diff(nums):
  nums.sort()
  ...
# .sort modifies the list which affects the list outside the function min_diff
  # nums.sort() -> nums = [1, 3, 4, 7, 9]
  # sorted(nums) -> nums = [4, 1, 7, 3, 9]

# Hashing vs Sorting
# you are given a list of numbers. how many distinct numbers does it contain
# list = [3,1,2,1,5,2,2,3], a=4
import random
import time

# algorithm 1 using a set
def count_distinct1(nums):
  seen = set()
  for n in nums:
    seen.add(n)
  return len(seen)
# time complex O(n)

# algorithm2 using sort()
def count_distinct2(nums):
  nums = sorted(nums)

  res = 1
  for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
      res += 1
  
  return res
# time complex O(n logn)

# now let us do a comparisson between both since they are both efficient
# inputs = 10^7. The input contains random numbers in the range 1...k
def test_time():
  random.seed(1337)
  numbers = [random.randint(1, 10) for _ in range(10**6)]

  start_time = time.time()
  result = count_distinct2(numbers)
  end_time = time.time()

  print("result: ", result)
  print("time: ", round(end_time - start_time, 2), "s")
  print("--------------------------------------------------")
# in this case, the algorithm 1 seems to be more efficient, shorter and simpler
# algorithm1: n= 10**6 || time: 0.03
# algorithm1: n= 10**7 || time: 0.34
# algorithm1: n= 10**9 || time: 3.26

# algorithm2: n= 10**6 || time: 0.11
# algorithm2: n= 10**7 || time: 1.12
# algorithm2: n= 10**9 || time: NaN

# More about sorting
# Sorting into reverse order
numbers = [2, 4, 3, 5, 6, 1, 8, 7]
numbers.sort(reverse=True)
print(numbers)
print("--------------------------------------------------")

# Element comparisons
# the parameter "key" can be used for defining a funciton that is applied to each eelement before 
# any comparison.
numbers = [4,-1,6,2,-7,8,3,-5]
numbers.sort(key=abs)
print(numbers)
print("--------------------------------------------------")

# Own class
# In python, objects of a class can be sorted if the class defines sufficient methods for comparing objs.
# __eq__ and __lt__, which are called when the objects are compared with the operators == and <
class Location:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __eq__(self, other):
    return (self.x, self.y) == (other.x, other.y)
  def __lt__(self, other):
    return(self.x, self.y) < (other.x, other.y)
  def __repr__(self):
    return str((self.x, self.y))

locations = []
locations.append(Location(1, 4))
locations.append(Location(4, 5))
locations.append(Location(2, 2))
locations.append(Location(1, 2))

locations.sort()

print(locations)
print("--------------------------------------------------")

# Example: Restaurant
# A restaurant is visited by n customers during a given day, and you know the arrival and departure time
# of each customer. If a customer departs at the same moment as another arrives, they are both considered
# to be in the restaurant at that moment. You rtask is to find out the highest number of customers that 
# are in the restaurant at the same time

# Customer | Arrival | Departure
# 1        | 6       | 8
# 2        | 3       | 7
# 3        | 6       | 9
# 4        | 1       | 5 
# 5        | 2       | 8

# a=4 -> 1,2,3,5 are in the restaurant during 6-7

# time | event | count
# 1    | 4a    | 1
# 2    | 5a    | 2
# 3    | 2a    | 3
# 4    | 4d    | 2
# 5    | 1a    | 3
# 6    | 2d    | 4
# 6    | 2d    | 3
# 7    | 1d    | 2
# 8    | 5d    | 1
# 9    | 3d    | 0

def max_customers(a, d):
  events = []
  for time in a:
    events.append((time,1))
  for time in d:
    events.append((time,2))
  
  events.sort()

  count = 0
  res = 0

  for event in events:
    if event[1] == 1:
      count += 1
    if event[1] == 2:
      count -= 1
    res = max(res, count)
  
  return res

print(max_customers([6, 3, 6, 1, 2],[8, 7, 9, 5, 8]))
print("--------------------------------------------------")
# Algorithm consists of 3 parts.
  # 1.Create a list of events O(n)
  # 2.Sorting the events lists O(n log n)
  # 3.Iterating through the events O(n)

# What happens during sorting
import functools

def cmp(a, b):
  print("compare", a, b)
  return a - b

numbers = [4, 1, 3, 2]
numbers.sort(key=functools.cmp_to_key(cmp))
print(numbers)
print("--------------------------------------------------")