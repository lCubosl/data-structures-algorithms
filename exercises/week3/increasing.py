# You are given a list of integers. Your task is to count how many sublists are increasing, i.e., where 
# each number is greater than the preceding number. Sublists of length one are counted too.

# For example, if the list is [2, 1, 3, 4], the increasing sublists are [1], [2], [3], [4], [1,3], [3,4] 
# and [1,3,4]. Thus the desired answer is 7.

# In a file increasing.py, implement the function count_sublists that takes a list of numbers as a 
# parameter and returns the count of increasing sublists.

# You must implement an efficient solution with a time complexity O(n). You cannot afford to go through 
# all sublists separately. Your solution should go through the input list only once.

# In the last test case of the following code template, the list is [1,2,\dots,10^5] and thus all 
# sublists are increasing. Your function should finish quickly in this test case too.

def count_sublists(numbers):
  count = 0
  run = 1

  for num in range(len(numbers)):
    if numbers[num] > numbers[num - 1]:
      run +=1
    else:
      run = 1  
    count+=run
  
  return count

print(count_sublists([2, 1, 3, 4])) # 7
print(count_sublists([1, 2, 3, 4])) # 10
print(count_sublists([4, 3, 2, 1])) # 4
print(count_sublists([1, 1, 1, 1])) # 4
print(count_sublists([1, 2, 1, 2])) # 6

numbers = list(range(1, 10**5+1))
print(count_sublists(numbers)) # 5000050000