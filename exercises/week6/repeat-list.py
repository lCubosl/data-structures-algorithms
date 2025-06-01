# Your task is to implement a class that maintains a list of numbers and has an efficient method that 
# reports if some number occurs more than once on the list.

# In a file repeatlist.py, implement the class RepeatList with the following methods:
  # append(number): add a number to the end of the list
  # repeat(): return True if some number repeats on the list, otherwise return False

# Both methods should work in O(1) time
class RepeatList:
  def __init__(self):
    self.numbers = []
    self.seen = set()
    self.repeated = False

  def append(self, number):
    if number in self.seen:
      self.repeated = True
    else:
      self.seen.add(number)
    self.numbers.append(number)

  def repeat(self):
    return self.repeated

numbers = RepeatList()

print(numbers.repeat()) # False

numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers.repeat()) # False

numbers.append(2)
print(numbers.repeat()) # True

numbers.append(5)
print(numbers.repeat()) # True

# Here the numbers 1, 2 and 3 are first added to the list so that the list content is [1,2,3] and there 
# is no repeating number. Then the number 2 is added to the list resulting in the content [1,2,3,2] with 
# a repeat of the number 2. Finally, the number 5 is added resulting in the content [1,2,3,2,5] with the number 2 still repeating.

# You can test the efficiency of your solution with the following code. In this case too the code should 
# finish almost immediately.
numbers = RepeatList()
total = 0
for i in range(10**5):
    numbers.append(i * 999983 % 12345)
    if numbers.repeat():
        total += 1
print(total) # 87655