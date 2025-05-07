# You are given a list of integers. The list contains n-1 copies of the same number and a single copy of 
# another number. Your task is to find what number occurs only once.

# For example, when the list is [2, 1, 1, 1], the desired number is 2. Similarly, when the list is 
# [5, 5, 5, 3, 5], the number to find is 3.

# In a file onlyone.py, implement the function find_number that takes the list of numbers as a parameter 
# and returns the number with one occurrence only. You may assume that the list contains at least three 
# numbers so that the answer is always unique.

# You must implement an efficient solution with a time complexity O(n). For example, you cannot afford 
# to go through all numbers on the list and count the occurrences of each number separately.

# In the last test case of the following code template, the list contains 10^5 copies of the number 1 
# and one copy of the number 2. Your function should finish quickly in this test case too.

def find_number(numbers):
  counts = {}

  for num in numbers:
    if num in counts:
      counts[num] += 1
    else:
      counts[num] = 1
  
  return min(counts, key=counts.get)

# prints
print(find_number([1, 1, 1, 2])) # 2
print(find_number([1, 1, 2, 1])) # 2
print(find_number([1, 2, 1, 1])) # 2
print(find_number([2, 1, 1, 1])) # 2
print(find_number([5, 5, 5, 3, 5])) # 3
print(find_number([1, 100, 1])) # 100

numbers = [1] * 10**5 + [2]
print(find_number(numbers)) # 2