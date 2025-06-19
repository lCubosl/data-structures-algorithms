# Your task is to implement a class that maintains a list of numbers and has a method for efficiently computing the sum of distances 
# between all pairs of occurrences of a given number.

# For example, when the list is [1,2,1,3,3,1,2,1], the distances for the number 1 are:
  # positions 0 and 2: distance 2
  # positions 0 and 5: distance 5
  # positions 0 and 7: distance 7
  # positions 2 and 5: distance 3
  # positions 2 and 7: distance 5
  # positions 5 and 7: distance 2

# Thus the sum of the distances is 2+5+7+3+5+2=24.
# In a file distances.py, implement the class DistanceTracker with the methods:
  # append(number): add number to the end of the list
  # sum(number): return the sum of distances for number

# Both methods should work in O(1) time.
class DistanceTracker:
  def __init__(self):
    self.numbers = {}
    self.prefix = {}

  def append(self, number):
    index = sum(len(i) for i in self.numbers.values())

    if number not in self.numbers:
      self.numbers[number] = []
      self.prefix[number] = []
    
    self.numbers[number].append(index)
    print("numbers", self.numbers)

    prev_sum = self.prefix[number][-1] if  self.prefix[number] else 0
    self.prefix[number].append(prev_sum + index)
    print("prefix", self.prefix)

  def sum(self, number):
    pass
    # if number not in self.prefix:
    #   return 0    
    # return sum(self.prefix[number])

tracker = DistanceTracker()

tracker.append(1)
tracker.append(2)
tracker.append(1)
tracker.append(3)
tracker.append(3)
tracker.append(1)
tracker.append(2)
tracker.append(1)

print(tracker.sum(1)) # 24
print(tracker.sum(2)) # 5
print(tracker.sum(3)) # 1

tracker.append(1)
tracker.append(2)
tracker.append(3)

print(tracker.sum(1)) # 42
print(tracker.sum(2)) # 16
print(tracker.sum(3)) # 14

# If a number does not appear on the list or appears only once, the desired result is 0:
tracker = DistanceTracker()
print(tracker.sum(1)) # 0
tracker.append(1)
print(tracker.sum(1)) # 0

# You can test the efficiency of your solution with the following code. In this case too the code should finish almost immediately.
tracker = DistanceTracker()
total = 0
for i in range(10**5):
  tracker.append(1)
  total += tracker.sum(1)
print(total) # 4166749999583325000