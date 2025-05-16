# In the course material, there is an example for week 4 of an algorithm using a dictionary for finding a mode of a list.

# Another efficient way to find a mode is to sort the elements and go through the list from left to right while keeping track 
# of how many times each element is repeated.

# Compare the efficiency of the above two solutions for an input list containing 10^7 random numbers in the range 1 \dots 1000.

# In this task you get a point automatically, when you fill in your results and the code you used, and press the submit button.

# Running time for the dictionary implementation:  2.942s 82746
# Running time for the sorting implementation:     4.403s 82746

# The code you used in the test:
import random
import time

# week 4 - finding mode in the list
def find_mode(numbers):
  start_time = time.time()
  
  count = {}
  mode = numbers[0]

  for x in numbers:
    if x not in count:
      count[x] = 1
    count[x] += 1

    if count[x] > count[mode]:
      mode = x
      
  end_time = time.time()
  print("list time:", round(end_time-start_time, 3), "s")
  
  return mode

# go through the list from left to right while keeping track of how many times each element is repeated
def find_mode1(numbers):
  start_time = time.time()
  
  counts = {}
  prev = None

  ordered = sorted(numbers)
  for num in ordered:
    if num == prev:
      counts[num] += 1
    else:
      counts[num] = 1
      prev = num    
  mode = max(counts, key=counts.get)

  end_time = time.time()
  print("list time:", round(end_time-start_time, 3), "s")

  return mode

random.seed(1337)
n = 10000000
list = [random.randint(1, 10**5) for _ in range(n)]
print(find_mode(list))