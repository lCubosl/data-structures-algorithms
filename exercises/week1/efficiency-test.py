# The course material includes two different ways to implement the function count_even:
# implementation 1

def count_even1(numbers):
  result = 0
  for x in numbers:
    if x % 2 == 0:
      result += 1
  return result

# implementation 2
def count_even2(numbers):
  return sum(x % 2 == 0 for x in numbers)

# Compare the efficiencies of the two implementations using a list that contains 10^7 randomly chosen 
# numbers.

# In this exercise, you get a point automatically when you submit the test results and the code that 
# you used.

# implementation 1 run time: n = 10^7, time = 4.901s
# implementation 2 run time: n = 10^7, time = 6,625s

# writ the code you used bellow here:
import random
import time

n = 100000000
print("n:",n)
random.seed(1337)
numbers = [random.randint(1, 10**6) for _ in range(n)]

start_time = time.time()
resulut = count_even2(numbers)
end_time = time.time()

print("result:", resulut)
print(numbers)
print("time:", round(end_time - start_time, 3), "s")