# Your task is to implement a class that maintains a list of numbers and has a method for efficiently 
# incrementing all elements of the list by a given amount.

# In a file changelist.py, implement the class ChangeList with the following methods:
  # append(number): add number to the end of the list
  # get(index): access a number on the list
  # change_all(amount): increment all list numbers by amount

# In the method change_all, the parameter amount can be negative too, in which case all numbers are 
# decremented. All methods should work in O(1) time.

class ChangeList:
  def __init__(self):
    self.numbers = []
    self.increment = 0

  def append(self, number):
    self.numbers.append(number - self.increment)

  def get(self, index):
    return self.numbers[index] + self.increment

  def change_all(self, amount):
    self.increment += amount

numbers = ChangeList()

numbers.append(1)
numbers.append(2)
numbers.append(3)

print(numbers.get(0)) # 1
print(numbers.get(1)) # 2
print(numbers.get(2)) # 3

numbers.change_all(2)
print(numbers.get(0)) # 3
print(numbers.get(1)) # 4
print(numbers.get(2)) # 5

numbers.append(8)
numbers.change_all(-1)
print(numbers.get(0)) # 2
print(numbers.get(1)) # 3
print(numbers.get(2)) # 4
print(numbers.get(3)) # 7

# Here the numbers 1, 2 and 3 are first added to the list, after which the list contents are [1,2,3]. 
# Then all numbers are incremented by 2, after which the list contents are [3,4,5]. Finally, the number 
# 8 is added to the list and all numbers are changed by -1, after which the list contents are 
# [2,3,4,7].

# You can test the efficiency of your solution with the following code. In this case too the code should 
# finish almost immediately.
numbers = ChangeList()
total = 0
for i in range(10**5):
    numbers.append(i + 1)
    numbers.change_all(i % 11 - 5)
    total += numbers.get(i // 2)
print(total) # 2500049970