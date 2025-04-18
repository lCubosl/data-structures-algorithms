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

