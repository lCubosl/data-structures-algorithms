# Your task is to implement a class that maintains a list of numbers  and has a method that efficiently 
# computes the sum of the numbers in a given sublist.

# In a file sumlist.py, implement the class SumList with the following methods:
  # append(number): add number to the end of the list
  # sum(a, b): return the sum of the numbers from the position a to the position b

# Both methods should work in O(1) time.
class SumList:
  def __init__(self):
    self.numbers = []
    self.prefix = [0]

  def append(self, number):
    self.numbers.append(number)
    self.prefix.append(self.prefix[-1] + number)

  def sum(self, a, b):
    return self.prefix[b+1] - self.prefix[a]

numbers = SumList()

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

print(numbers.sum(0, 4)) # 15
print(numbers.sum(1, 1)) # 2
print(numbers.sum(1, 3)) # 9
print(numbers.sum(2, 3)) # 7
print(numbers.sum(0, 3)) # 10

numbers.append(1)
print(numbers.sum(0, 5)) # 16
print(numbers.sum(5, 5)) # 1

# Here the list content is first set to [1,2,3,4,5] and then the following sublist sums are 
# computed:
  # [1,2,3,4,5]: sum 15
  # [2]: sum 2
  # [2,3,4]: sum 9
  # [3,4]: sum 7
  # [1,2,3,4]: sum 10

# Then the number 1 is added to the end of the list and the following sublist sums are computed:
  # [1,2,3,4,5,1]: sum 16
  # [1]: sum 1

# You can test the efficiency of your solution with the following code. In this case too the code should finish almost immediately.
numbers = SumList()
total = 0
for i in range(10**5):
    numbers.append(i + 1)
    total += numbers.sum(i // 2, i)
print(total) # 125005000050000