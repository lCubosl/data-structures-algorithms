# Your task is to implement a class that maintains a list of numbers and has a method for efficiently 
# finding the largest number on the list.
# In a file maxlist.py, implement the class MaxList with the following methods:

  # append(number): add a number to the end of the list
  # max(): return the largest number

# You may assume that the list has at least one number when the method max is called. Both methods should 
# work efficiently in O(1) time.

class MaxList:
  def __init__(self):
    pass  

  def append(self, number):
    pass

  def max(self):
    pass

numbers = MaxList()

numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers.max()) # 3

numbers.append(8)
numbers.append(5)
print(numbers.max()) # 8

# Here the elements 1, 2 and 3 are first added to the list so that the list content is [1,2,3] and the 
# largest number is 3. Then the numbers 8 and 5 are added to the list resulting in the content 
# [1,2,3,8,5] and the largest number 8.

# You can test the efficiency of your solution with the following code. In this case too the code should 
# finish almost immediately.
numbers = MaxList()
total = 0
for i in range(10**5):
  numbers.append(i * 999983 % 10**9)
  total += numbers.max()
print(total) # 99498381797517