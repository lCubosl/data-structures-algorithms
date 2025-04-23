# https://tira.mooc.fi/spring-2024/chap01/#efficiency-of-algorithms
# what is an algorithm
def count_even(numbers):
  result = 0
  for x in numbers:
    if x % 2 == 0:
      result += 1
  
  return result

print(count_even([1, 2, 3])) # 1
print(count_even([2, 2, 2, 2, 2])) # 5
print(count_even([5, 4, 1, 7, 9, 6])) # 2

# This can be implemented more compactly with a special Python construct, the generator expression:
def count_even(numbers):
  return sum(x % 2 == 0 for x in numbers)

print(count_even([1, 2, 3])) # 1
print(count_even([2, 2, 2, 2, 2])) # 5
print(count_even([5, 4, 1, 7, 9, 6])) # 2
print("\n")

# Efficiency of algorithms
# The algorithm 1 has two nested for loops that go through all ways of choosing two numbers from the list. 
# The algorithm computes the difference using the abs (absolute value) function and remembers the largest 
# difference it has encounter so far.

# 1
def max_diff1(numbers):
  result = 0
  for x in numbers:
    for y in numbers:
      result = max(result, abs(x - y))
  
  return result

print(max_diff1([3, 2, 6, 5, 8, 5]))

# The idea of the algorithm 2 is that the biggest difference must be between the smallest number and 
# the largest number on the list.
# The algorithm first sorts the list using the sorted function. Then the smallest number is in the beginning 
# (index 0) and the largest is at the end (index -1) of the list.

# 2
def max_diff2(numbers):
  numbers = sorted(numbers)
  return numbers[-1] - numbers[0]

# The algorithm 3 is based on finding the smallest and largest numbers too, but instead of sorting, it uses the functions min 
# and max.

# 3
def max_diff3(numbers):
  return max(numbers) - min(numbers)

# Below is a program that tests the efficiency of the max_diff function:
import random
import time

n = 1000
print("n: ", n)
random.seed(1337)
numbers = [random.randint(1, 10**6) for _ in range(n)]

start_time = time.time()
result = max_diff3(numbers)
end_time = time.time()

print("result: ", result)
print("time: ", round(end_time - start_time, 2), "s")
print("--------------------------------------------------")

# time complexity (common complexities)
# O(1) Contstant 
# O(logn) Logarithmic
# O(n) Linear
# O(n logn) 
# O(n^2) Quadratic
# O(n^3) Cubic

# Constant: If algo has no loops and executes the same steps idnependent of the input
# O(1)
def middle(numbers):
  n = len(numbers)
  return numbers[n // 2]

# single loop
# Linear: Single Loop that goes through all elements of the input ONLY ONCE
# O(n)
def calc_sum(numbers):
  result = 0
  for x in numbers:
    result += x
  return result

# Nested loops
# Quadratic: If algorithm contains loop inside a loop, each of each goes through all elements of the input
# O(n^2)
def has_sum(numbers, x):
  for a in numbers:
    for b in numbers:
      if a + b == x:
        return True
  return False

# Sequential code segments
# If the agorithm consists of multiple code segments in sequence, the time complexity is the maximum 
# of the segment time complexities
# O(n)

def count_min(numbers):
  min_val = numbers[0]
  for x in numbers:
    if x < min_val:
      min_val = x
    
  result = 0
  for x in numbers:
    if x == min_val:
      result += 1
  
  return result

  